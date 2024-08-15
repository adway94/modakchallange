# Rate-Limited Notification Service

## Overview

This project implements a rate-limited notification service in Python. The service is designed to send various types of notifications (e.g., status updates, news, marketing) while enforcing rate limits to prevent overwhelming recipients with too many messages.

## Features

- Send different types of notifications (status, news, marketing, etc.)
- Implement rate limiting for each notification type
- Handle various exceptions for better error management
- Modular and extensible design

## Project Structure

```
.
├── notification_service/
│   ├── __init__.py
│   ├── exceptions.py
│   ├── models.py
│   └── services.py
├── tests/
│   ├── __init__.py
│   └── test.py
├── __init__.py
├── main.py
└── README.md
```

- `notification_service/`: Main package for the notification service
  - `__init__.py`: Package initializer
  - `exceptions.py`: Contains custom exception classes
  - `models.py`: Defines notification classes
  - `services.py`: Implements the core notification service and rate limiter
- `tests/`: Directory containing all test files
  - `__init__.py`: Package initializer for tests
  - `test.py`: Contains unit tests for the notification service
- `__init__.py`: Root package initializer
- `main.py`: Entry point with usage examples
- `README.md`: This file, containing project documentation

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/rate-limited-notification-service.git
   cd rate-limited-notification-service
   ```

2. (Optional) Create and activate a virtual environment:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

## Usage

Here's a basic example of how to use the notification service:

```python
from notification_service.services import NotificationService

# Create a notification service instance
service = NotificationService()

# Send a status notification
service.send_notification("user@example.com", "status", "Status update message")

# Send a news notification
service.send_notification("user@example.com", "news", "Daily news update")

# Send a marketing notification
service.send_notification("user@example.com", "marketing", "Special offer!")
```

## Rate Limits

The current rate limits are set as follows:

- Status: 2 per minute for each recipient
- News: 1 per day for each recipient
- Marketing: 3 per hour for each recipient

These limits can be adjusted in the `NotificationService._check_rate_limit` method.

## Exception Handling

The service includes custom exceptions to handle various error scenarios:

- `RateLimitExceededException`: Thrown when a rate limit is exceeded
- `InvalidNotificationTypeException`: Thrown when an unknown notification type is used
- `NotificationSendException`: Thrown when there's an error sending a notification

## Extending the Service

To add a new notification type:

1. Update the `NotificationService._check_rate_limit` method to include the new type and its rate limit.
2. If needed, create a new notification class in `models/__init__.py`.

## Running Tests

To run the unit tests for this project, use the following command:

```
python -m unittest tests.py
```

This will run all the tests defined in the `tests.py` file and show you the results.
