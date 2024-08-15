class NotificationException(Exception):
    """Exceptions for the notifications errors"""
    pass

class RateLimitExceededException(NotificationException):
    """It launchs when the limit it is exceded"""
    def __init__(self, recipient: str, notification_type: str):
        self.recipient = recipient
        self.notification_type = notification_type
        super().__init__(f"Rate limit exceeded for recipient {recipient} on {notification_type} notifications")

class InvalidNotificationTypeException(NotificationException):
    """It launchs when try to use a non recognized notification type."""
    def __init__(self, notification_type: str):
        self.notification_type = notification_type
        super().__init__(f"Invalid notification type: {notification_type}")

class NotificationSendException(NotificationException):
    """It launch when there is a error when sending the notification."""
    def __init__(self, recipient: str, notification_type: str, error: str):
        self.recipient = recipient
        self.notification_type = notification_type
        self.error = error
        super().__init__(f"Error sending {notification_type} notification to {recipient}: {error}")