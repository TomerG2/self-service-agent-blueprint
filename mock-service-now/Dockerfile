# Mock ServiceNow Server Dockerfile
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN pip install uv

# Copy project files
COPY pyproject.toml ./
COPY src/ ./src/

# Install dependencies
RUN uv pip install --system -e .

# Create non-root user
RUN useradd --create-home --shell /bin/bash mockuser && \
    chown -R mockuser:mockuser /app
USER mockuser

# Expose port
EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
    CMD curl -f http://localhost:8080/health || exit 1

# Run the server
CMD ["uvicorn", "mock_servicenow.server:app", "--host", "0.0.0.0", "--port", "8080"]