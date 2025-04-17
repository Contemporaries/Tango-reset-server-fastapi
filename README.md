# TO DO （MCP Server）Under development
Connect to MCP (Model Context Protocol) and drive it with a large model
Test Result：
![Screenshot 2025-04-15 160102](https://github.com/user-attachments/assets/515da645-7ad3-4b53-af91-86bcd784e29d)


# Tango REST API based on FastAPI

A REST API service based on FastAPI and PyTango for interacting with Tango devices.

## System Requirements

- Python 3.8+
- Tango server environment

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Contemporaries/Tango-rest-server-fastapi.git
cd Tango-rest-server-fastapi
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## API Doc
http(s)://your_host:8000/docs

## Project Structure

```
IHEP-Tango-Rest-API/
├── assets/          # Static resource files
├── config/          # Configuration files
│   ├── env_config.py   # Environment variable configuration
│   ├── log_config.py   # Log configuration
├── controller/      # API controllers
│   ├── controller_attribute.py   # Attribute-related interfaces
│   ├── controller_command.py     # Command-related interfaces
│   ├── controller_db.py         # Database-related interfaces
│   ├── controller_info.py       # Information query interfaces
│   ├── controller_polling.py    # Polling-related interfaces
│   └── controller_property.py   # Property configuration interfaces
|   └── controller_env.py       # Environment variable interfaces
├── exception/       # Exception handling
├── model/          # Data models
├── service/        # Business logic layer
│   ├── service_attribute.py     # Attribute services
│   ├── service_command.py       # Command services
│   ├── service_db.py           # Database services
│   ├── service_info.py         # Information query services
│   ├── service_polling.py      # Polling services
│   └── service_property.py     # Property configuration services
│   └── service_env.py       # Environment variable services
├── test/           # Test files
├── tools/          # Utility functions
├── enums/          # Enum definitions
├── main.py         # Application entry point
└── requirements.txt # Project dependencies
└── .env            # Environment variables
```


## Development Guide

### 1. Adding New APIs

1. Create a new controller file in the `controller` directory
2. Implement business logic in the `service` directory
3. Register the route in `main.py`

### 2. Error Handling

Use `GlobalException` for unified error handling:

```python
from exception.global_exception import GlobalException

try:
    # Business logic
except Exception as e:
    raise GlobalException(str(e))
```

### 3. Response Model

Use `ResponseModel` to ensure a unified response format:

```python
from model.response_models import ResponseModel

return ResponseModel(
    code: int
    success: bool
    message: str | None = None
    data: dict | str | list | int | bool | None = None
)
```
