from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, recipient: str, content: str):
        pass

class EmailNotification(Notification):
    def send(self, recipient: str, content: str):
        from notification_service.exceptions import NotificationSendException
        # Simulate a posible error
        if "invalid" in recipient:
            raise NotificationSendException(recipient, "email", "Invalid email address")
        print(f"Sending email to {recipient}: {content}")