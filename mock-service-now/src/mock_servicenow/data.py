"""Mock data for ServiceNow API responses."""

import random
from datetime import datetime
from typing import Any, Dict, List

# Mock employee and laptop data - adapted from the MCP server mock data
MOCK_EMPLOYEE_DATA = {
    "alice.johnson@company.com": {
        "employee_id": "1001",
        "sys_id": "1001",
        "name": "Alice Johnson",
        "email": "alice.johnson@company.com",
        "user_name": "alice.johnson",
        "location": "EMEA",
        "active": "true",
        "laptop_model": "Latitude 7420",
        "laptop_serial_number": "DL7420001",
        "purchase_date": "2020-01-15",
        "warranty_expiry": "2023-01-15",
        "warranty_status": "Expired",
        "asset_tag": "ASSET-001",
        "model_id": "latitude_7420",
        "install_status": "1",
        "operational_status": "1",
    },
    "john.doe@company.com": {
        "employee_id": "1002",
        "sys_id": "1002",
        "name": "John Doe",
        "email": "john.doe@company.com",
        "user_name": "john.doe",
        "location": "EMEA",
        "active": "true",
        "laptop_model": "MacBook Pro 14-inch",
        "laptop_serial_number": "MBP14002",
        "purchase_date": "2023-03-20",
        "warranty_expiry": "2026-03-20",
        "warranty_status": "Active",
        "asset_tag": "ASSET-002",
        "model_id": "macbook_pro_14",
        "install_status": "1",
        "operational_status": "1",
    },
    "maria.garcia@company.com": {
        "employee_id": "1003",
        "sys_id": "1003",
        "name": "Maria Garcia",
        "email": "maria.garcia@company.com",
        "user_name": "maria.garcia",
        "location": "LATAM",
        "active": "true",
        "laptop_model": "ThinkPad X1 Carbon",
        "laptop_serial_number": "TP1C003",
        "purchase_date": "2022-11-10",
        "warranty_expiry": "2025-11-10",
        "warranty_status": "Active",
        "asset_tag": "ASSET-003",
        "model_id": "thinkpad_x1_carbon",
        "install_status": "1",
        "operational_status": "1",
    },
    "oliver.smith@company.com": {
        "employee_id": "1004",
        "sys_id": "1004",
        "name": "Oliver Smith",
        "email": "oliver.smith@company.com",
        "user_name": "oliver.smith",
        "location": "EMEA",
        "active": "true",
        "laptop_model": "EliteBook 840 G7",
        "laptop_serial_number": "HP840004",
        "purchase_date": "2019-05-12",
        "warranty_expiry": "2022-05-12",
        "warranty_status": "Expired",
        "asset_tag": "ASSET-004",
        "model_id": "elitebook_840_g7",
        "install_status": "1",
        "operational_status": "1",
    },
    "yuki.tanaka@company.com": {
        "employee_id": "1005",
        "sys_id": "1005",
        "name": "Yuki Tanaka",
        "email": "yuki.tanaka@company.com",
        "user_name": "yuki.tanaka",
        "location": "APAC",
        "active": "true",
        "laptop_model": "XPS 13 9310",
        "laptop_serial_number": "DL13005",
        "purchase_date": "2018-09-03",
        "warranty_expiry": "2021-09-03",
        "warranty_status": "Expired",
        "asset_tag": "ASSET-005",
        "model_id": "xps_13_9310",
        "install_status": "1",
        "operational_status": "1",
    },
    "isabella.mueller@company.com": {
        "employee_id": "1006",
        "sys_id": "1006",
        "name": "Isabella Mueller",
        "email": "isabella.mueller@company.com",
        "user_name": "isabella.mueller",
        "location": "EMEA",
        "active": "true",
        "laptop_model": "ThinkPad T14",
        "laptop_serial_number": "TP14006",
        "purchase_date": "2019-11-18",
        "warranty_expiry": "2022-11-18",
        "warranty_status": "Expired",
        "asset_tag": "ASSET-006",
        "model_id": "thinkpad_t14",
        "install_status": "1",
        "operational_status": "1",
    },
    "carlos.rodriguez@company.com": {
        "employee_id": "1007",
        "sys_id": "1007",
        "name": "Carlos Rodriguez",
        "email": "carlos.rodriguez@company.com",
        "user_name": "carlos.rodriguez",
        "location": "LATAM",
        "active": "true",
        "laptop_model": "MacBook Air M1",
        "laptop_serial_number": "MBA1007",
        "purchase_date": "2021-02-14",
        "warranty_expiry": "2024-02-14",
        "warranty_status": "Active",
        "asset_tag": "ASSET-007",
        "model_id": "macbook_air_m1",
        "install_status": "1",
        "operational_status": "1",
    },
    "david.chen@company.com": {
        "employee_id": "1008",
        "sys_id": "1008",
        "name": "David Chen",
        "email": "david.chen@company.com",
        "user_name": "david.chen",
        "location": "APAC",
        "active": "true",
        "laptop_model": "ZenBook Pro 15",
        "laptop_serial_number": "AS15008",
        "purchase_date": "2020-07-22",
        "warranty_expiry": "2023-07-22",
        "warranty_status": "Expired",
        "asset_tag": "ASSET-008",
        "model_id": "zenbook_pro_15",
        "install_status": "1",
        "operational_status": "1",
    },
    "sophie.dubois@company.com": {
        "employee_id": "1009",
        "sys_id": "1009",
        "name": "Sophie Dubois",
        "email": "sophie.dubois@company.com",
        "user_name": "sophie.dubois",
        "location": "EMEA",
        "active": "true",
        "laptop_model": "Surface Laptop 4",
        "laptop_serial_number": "MS4009",
        "purchase_date": "2021-08-05",
        "warranty_expiry": "2024-08-05",
        "warranty_status": "Active",
        "asset_tag": "ASSET-009",
        "model_id": "surface_laptop_4",
        "install_status": "1",
        "operational_status": "1",
    },
    "ahmed.hassan@company.com": {
        "employee_id": "1010",
        "sys_id": "1010",
        "name": "Ahmed Hassan",
        "email": "ahmed.hassan@company.com",
        "user_name": "ahmed.hassan",
        "location": "EMEA",
        "active": "true",
        "laptop_model": "Inspiron 15 5000",
        "laptop_serial_number": "DL15010",
        "purchase_date": "2018-03-14",
        "warranty_expiry": "2021-03-14",
        "warranty_status": "Expired",
        "asset_tag": "ASSET-010",
        "model_id": "inspiron_15_5000",
        "install_status": "1",
        "operational_status": "1",
    },
    "jane.smith@company.com": {
        "employee_id": "2001",
        "sys_id": "2001",
        "name": "Jane Smith",
        "email": "jane.smith@company.com",
        "user_name": "jane.smith",
        "location": "San Francisco Office",
        "active": "true",
        "laptop_model": "MacBook Pro 16-inch",
        "laptop_serial_number": "DEF789012",
        "purchase_date": "2023-01-10",
        "warranty_expiry": "2026-01-10",
        "warranty_status": "Active",
        "asset_tag": "ASSET-011",
        "model_id": "macbook_pro_16",
        "install_status": "1",
        "operational_status": "1",
    },
    "bob.wilson@company.com": {
        "employee_id": "2002",
        "sys_id": "2002",
        "name": "Bob Wilson",
        "email": "bob.wilson@company.com",
        "user_name": "bob.wilson",
        "location": "London Office",
        "active": "true",
        "laptop_model": "HP EliteBook 850",
        "laptop_serial_number": "JKL901234",
        "purchase_date": "2023-09-05",
        "warranty_expiry": "2026-09-05",
        "warranty_status": "Active",
        "asset_tag": "ASSET-012",
        "model_id": "elitebook_850",
        "install_status": "1",
        "operational_status": "1",
    },
    "alice.brown@company.com": {
        "employee_id": "2003",
        "sys_id": "2003",
        "name": "Alice Brown",
        "email": "alice.brown@company.com",
        "user_name": "alice.brown",
        "location": "Tokyo Office",
        "active": "true",
        "laptop_model": "Lenovo ThinkPad X1 Carbon",
        "laptop_serial_number": "MNO567890",
        "purchase_date": "2022-11-12",
        "warranty_expiry": "2025-11-12",
        "warranty_status": "Active",
        "asset_tag": "ASSET-013",
        "model_id": "thinkpad_x1_carbon",
        "install_status": "1",
        "operational_status": "1",
    },
    "charlie.davis@company.com": {
        "employee_id": "2004",
        "sys_id": "2004",
        "name": "Charlie Davis",
        "email": "charlie.davis@company.com",
        "user_name": "charlie.davis",
        "location": "Sydney Office",
        "active": "true",
        "laptop_model": "Microsoft Surface Laptop 4",
        "laptop_serial_number": "PQR123456",
        "purchase_date": "2023-04-18",
        "warranty_expiry": "2026-04-18",
        "warranty_status": "Active",
        "asset_tag": "ASSET-014",
        "model_id": "surface_laptop_4",
        "install_status": "1",
        "operational_status": "1",
    },
    "tchughesiv@gmail.com": {
        "employee_id": "3001",
        "sys_id": "3001",
        "name": "Tommy Hughes",
        "email": "tchughesiv@gmail.com",
        "user_name": "tommy.hughes",
        "location": "New Orleans - Remote",
        "active": "true",
        "laptop_model": "MacBook Pro 16-inch",
        "laptop_serial_number": "TCH789012",
        "purchase_date": "2021-01-10",
        "warranty_expiry": "2024-01-10",
        "warranty_status": "Expired",
        "asset_tag": "ASSET-015",
        "model_id": "macbook_pro_16",
        "install_status": "1",
        "operational_status": "1",
    },
    "midawson@redhat.com": {
        "employee_id": "3002",
        "sys_id": "3002",
        "name": "Michael Dawson",
        "email": "midawson@redhat.com",
        "user_name": "michael.dawson",
        "location": "NA",
        "active": "true",
        "laptop_model": "MacBook Pro 16-inch",
        "laptop_serial_number": "TCH789111",
        "purchase_date": "2022-01-10",
        "warranty_expiry": "2025-01-10",
        "warranty_status": "Expired",
        "asset_tag": "ASSET-016",
        "model_id": "macbook_pro_16",
        "install_status": "1",
        "operational_status": "1",
    },
}


def generate_ticket_number() -> str:
    """Generate a mock ServiceNow ticket number."""
    # Generate 7-digit number to match ServiceNow format (e.g., REQ0010037)
    return f"REQ{random.randint(1000000, 9999999):07d}"


def find_user_by_email(email: str) -> Dict[str, Any] | None:
    """Find user by email address.

    Args:
        email: Email address to search for

    Returns:
        User data dictionary if found, None otherwise
    """
    if not email:
        return None

    user_data = MOCK_EMPLOYEE_DATA.get(email.lower())
    if not user_data:
        return None

    # Return ServiceNow-style user response
    return {
        "sys_id": user_data["sys_id"],
        "name": user_data["name"],
        "email": user_data["email"],
        "user_name": user_data["user_name"],
        "location": {
            "display_value": user_data["location"],
            "value": user_data["location"],
        },
        "active": user_data["active"],
    }


def find_computers_by_user_sys_id(user_sys_id: str) -> List[Dict[str, Any]]:
    """Find computers assigned to a user sys_id.

    Args:
        user_sys_id: User's sys_id

    Returns:
        List of computer data dictionaries
    """
    if not user_sys_id:
        return []

    # Find the user data by sys_id
    user_data = None
    for email, data in MOCK_EMPLOYEE_DATA.items():
        if data["sys_id"] == user_sys_id:
            user_data = data
            break

    if not user_data:
        return []

    # Return ServiceNow-style computer response
    return [
        {
            "sys_id": f"comp_{user_data['sys_id']}",
            "name": f"{user_data['name']}'s Laptop",
            "asset_tag": user_data["asset_tag"],
            "serial_number": user_data["laptop_serial_number"],
            "model_id": {
                "display_value": user_data["laptop_model"],
                "value": user_data["model_id"],
            },
            "assigned_to": user_sys_id,
            "purchase_date": user_data["purchase_date"],
            "warranty_expiration": user_data["warranty_expiry"],
            "install_status": user_data["install_status"],
            "operational_status": user_data["operational_status"],
        }
    ]


def create_laptop_refresh_request(
    laptop_refresh_id: str, laptop_choices: str, who_is_this_request_for: str
) -> Dict[str, Any]:
    """Create a mock laptop refresh request.

    Args:
        laptop_refresh_id: ServiceNow catalog item ID
        laptop_choices: Laptop model choice
        who_is_this_request_for: User sys_id

    Returns:
        ServiceNow-style response for ticket creation
    """
    ticket_number = generate_ticket_number()

    # Generate a mock sys_id for the request
    request_sys_id = f"req_{random.randint(100000, 999999)}"

    # ServiceNow-compatible response format
    return {
        "result": {
            "sys_id": request_sys_id,
            "request_number": ticket_number,
            "state": "1",  # Pending
            "stage": "requested",
            "opened_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "requested_for": who_is_this_request_for,
            "variables": {
                "laptop_choices": laptop_choices,
                "who_is_this_request_for": who_is_this_request_for,
            },
        }
    }
