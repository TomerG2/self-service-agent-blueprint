#!/bin/bash

# ServiceNow PDI Hibernation Detection and Wake-up Script
# This script checks if a ServiceNow PDI is hibernating and wakes it up if needed

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
MAX_WAKE_ATTEMPTS=3
WAKE_POLL_INTERVAL=30  # seconds
MAX_WAKE_WAIT=600      # 10 minutes total wait time

# Function to log with timestamp and color
log() {
    local color=$1
    local message=$2
    echo -e "${color}[$(date +'%Y-%m-%d %H:%M:%S')] ${message}${NC}"
}

log_info() {
    log "${BLUE}" "INFO: $1"
}

log_success() {
    log "${GREEN}" "SUCCESS: $1"
}

log_warning() {
    log "${YELLOW}" "WARNING: $1"
}

log_error() {
    log "${RED}" "ERROR: $1"
}

# Function to check if ServiceNow instance is hibernating
check_hibernation_status() {
    local base_url="$1"
    local api_key="$2"

    log_info "Checking hibernation status for: $base_url"

    local response
    local http_code

    # Make API call and capture both response and HTTP status code
    response=$(curl -s -w "\n%{http_code}" \
        -H "x-sn-apikey: $api_key" \
        -H "Accept: application/json" \
        "$base_url/api/now/ui/user/current_user" 2>/dev/null || echo "000")

    # Split response and HTTP code
    http_code=$(echo "$response" | tail -n1)
    body=$(echo "$response" | head -n -1)

    log_info "HTTP Status Code: $http_code"

    if [[ "$http_code" == "200" ]]; then
        if echo "$body" | grep -q "Instance Hibernating page"; then
            log_warning "Instance is hibernating"
            return 0  # Hibernating
        else
            log_success "Instance is awake and responding"
            return 1  # Awake
        fi
    else
        log_error "API call failed with HTTP $http_code"
        log_error "Response: $body"
        return 2  # Error
    fi
}

# Function to wake up ServiceNow instance
wake_up_instance() {
    log_info "Waking up ServiceNow instance..."

    # Run the servicenow-wake command
    if make servicenow-wake; then
        log_success "Wake-up command executed successfully"
        return 0
    else
        log_error "Wake-up command failed"
        return 1
    fi
}

# Function to wait for instance to be awake
wait_for_instance_awake() {
    local base_url="$1"
    local api_key="$2"
    local start_time=$(date +%s)
    local end_time=$((start_time + MAX_WAKE_WAIT))

    log_info "Waiting for instance to fully wake up (max ${MAX_WAKE_WAIT}s)..."

    while true; do
        local current_time=$(date +%s)

        if [[ $current_time -gt $end_time ]]; then
            log_error "Timeout: Instance did not wake up within ${MAX_WAKE_WAIT} seconds"
            return 1
        fi

        local elapsed=$((current_time - start_time))
        log_info "Checking status... (elapsed: ${elapsed}s)"

        check_hibernation_status "$base_url" "$api_key"
        local status=$?

        case $status in
            0)  # Still hibernating
                log_info "Instance still hibernating, waiting ${WAKE_POLL_INTERVAL}s..."
                sleep $WAKE_POLL_INTERVAL
                ;;
            1)  # Awake
                log_success "Instance is now fully awake!"
                return 0
                ;;
            2)  # Error
                log_warning "API check failed, will retry in ${WAKE_POLL_INTERVAL}s..."
                sleep $WAKE_POLL_INTERVAL
                ;;
        esac
    done
}

# Main function
main() {
    log_info "Starting ServiceNow PDI hibernation check..."

    # Validate all required environment variables
    local missing_vars=()

    [[ -z "${SERVICENOW_INSTANCE_URL:-}" ]] && missing_vars+=("SERVICENOW_INSTANCE_URL")
    [[ -z "${SERVICENOW_API_KEY:-}" ]] && missing_vars+=("SERVICENOW_API_KEY")
    [[ -z "${SERVICENOW_DEV_PORTAL_USERNAME:-}" ]] && missing_vars+=("SERVICENOW_DEV_PORTAL_USERNAME")
    [[ -z "${SERVICENOW_DEV_PORTAL_PASSWORD:-}" ]] && missing_vars+=("SERVICENOW_DEV_PORTAL_PASSWORD")

    if [[ ${#missing_vars[@]} -gt 0 ]]; then
        log_error "Required environment variables not set:"
        for var in "${missing_vars[@]}"; do
            log_error "  $var"
        done
        exit 1
    fi

    local base_url="$SERVICENOW_INSTANCE_URL"
    local api_key="$SERVICENOW_API_KEY"

    # Remove trailing slash from URL if present
    base_url="${base_url%/}"

    log_info "ServiceNow Instance URL: $base_url"

    # Initial hibernation check
    check_hibernation_status "$base_url" "$api_key"
    local initial_status=$?

    case $initial_status in
        0)  # Instance is hibernating
            log_warning "Instance is hibernating - attempting to wake it up"

            local attempt=1
            while [[ $attempt -le $MAX_WAKE_ATTEMPTS ]]; do
                log_info "Wake-up attempt $attempt/$MAX_WAKE_ATTEMPTS"

                if wake_up_instance; then
                    # Wait for instance to become fully awake
                    if wait_for_instance_awake "$base_url" "$api_key"; then
                        log_success "Instance successfully awakened!"
                        exit 0
                    else
                        log_error "Instance wake-up timed out on attempt $attempt"
                        attempt=$((attempt + 1))
                    fi
                else
                    log_error "Wake-up command failed on attempt $attempt"
                    attempt=$((attempt + 1))
                fi

                if [[ $attempt -le $MAX_WAKE_ATTEMPTS ]]; then
                    log_info "Waiting before next attempt..."
                    sleep 30
                fi
            done

            log_error "Failed to wake up instance after $MAX_WAKE_ATTEMPTS attempts"
            exit 1
            ;;
        1)  # Instance is awake
            log_success "Instance is already awake - no action needed"
            exit 0
            ;;
        2)  # API error
            log_error "Failed to check hibernation status"
            exit 1
            ;;
    esac
}

# Show help message
show_help() {
    cat << EOF
ServiceNow PDI Hibernation Detection and Wake-up Script

This script checks if a ServiceNow Personal Developer Instance (PDI) is hibernating
and automatically wakes it up if needed.

REQUIRED ENVIRONMENT VARIABLES:
  SERVICENOW_INSTANCE_URL        - Base URL of your ServiceNow instance
  SERVICENOW_API_KEY            - API key for ServiceNow instance
  SERVICENOW_DEV_PORTAL_USERNAME - ServiceNow Developer Portal username (for wake-up)
  SERVICENOW_DEV_PORTAL_PASSWORD - ServiceNow Developer Portal password (for wake-up)

USAGE:
  $0 [OPTIONS]

OPTIONS:
  -h, --help    Show this help message and exit

EXAMPLES:
  # Check and wake up instance if hibernating
  export SERVICENOW_INSTANCE_URL="https://dev12345.service-now.com"
  export SERVICENOW_API_KEY="your-api-key"
  export SERVICENOW_DEV_PORTAL_USERNAME="your-username"
  export SERVICENOW_DEV_PORTAL_PASSWORD="your-password"
  $0

EXIT CODES:
  0 - Success (instance awake or successfully awakened)
  1 - Failure (instance hibernating and could not wake up, or other error)

EOF
}

# Parse command line arguments
if [[ $# -gt 0 ]]; then
    case "$1" in
        -h|--help)
            show_help
            exit 0
            ;;
        *)
            log_error "Unknown option: $1"
            show_help
            exit 1
            ;;
    esac
fi

# Run main function
main "$@"