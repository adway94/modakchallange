
from datetime import datetime, timedelta
from collections import defaultdict
from typing import Dict, List
from notification_service.exceptions import RateLimitExceededException, InvalidNotificationTypeException, NotificationSendException
from notification_service.models import EmailNotification

class RateLimiter:
    """Checks the limits"""
    def __init__(self):
        self.limits: Dict[str, Dict[str, List[datetime]]] = defaultdict(lambda: defaultdict(list))

    def check_rate_limit(self, recipient: str, notification_type: str, limit: int, time_window: timedelta) -> bool:
        """This function check the rate limit

        Args:
            recipient (str): Destinatary of the mail
            notification_type (str): Notification type (news, status, etc)
            limit (int): Limit of messages 
            time_window (timedelta): Provided time between messages

        Returns:
            bool: Avaible to send or not
        """
        now = datetime.now()
        #Clean the notifications that are outside the time_window
        self.limits[recipient][notification_type] = [t for t in self.limits[recipient][notification_type] if now - t <= time_window]
        
        if len(self.limits[recipient][notification_type]) < limit:
            self.limits[recipient][notification_type].append(now)
            return True
        return False
    
class NotificationService:
    def __init__(self):
        self.rate_limiter = RateLimiter()
        self.notification_sender = EmailNotification()

    def send_notification(self, recipient: str, notification_type: str, content: str):
        try:
            if self._check_rate_limit(recipient, notification_type):
                self.notification_sender.send(recipient, content)
                return True
            else:
                raise RateLimitExceededException(recipient, notification_type)
        except RateLimitExceededException as e:
            print(f"Rate limit error: {str(e)}")
            return False
        except NotificationSendException as e:
            print(f"Send error: {str(e)}")
            return False
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            return False

    def _check_rate_limit(self, recipient: str, notification_type: str) -> bool:
        if notification_type == "status":
            return self.rate_limiter.check_rate_limit(recipient, notification_type, 2, timedelta(minutes=1))
        elif notification_type == "news":
            return self.rate_limiter.check_rate_limit(recipient, notification_type, 1, timedelta(days=1))
        elif notification_type == "marketing":
            return self.rate_limiter.check_rate_limit(recipient, notification_type, 3, timedelta(hours=1))
        else:
            raise InvalidNotificationTypeException(notification_type)
