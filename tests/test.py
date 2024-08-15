import unittest
from unittest.mock import patch
from datetime import timedelta
from notification_service.services import NotificationService, RateLimiter
from notification_service.exceptions import RateLimitExceededException, InvalidNotificationTypeException, NotificationSendException

class TestRateLimiter(unittest.TestCase):
    def setUp(self):
        self.rate_limiter = RateLimiter()

    def test_check_rate_limit_success(self):
        self.assertTrue(self.rate_limiter.check_rate_limit("user@example.com", "status", 2, timedelta(minutes=1)))
        self.assertTrue(self.rate_limiter.check_rate_limit("user@example.com", "status", 2, timedelta(minutes=1)))

    def test_check_rate_limit_exceeded(self):
        self.assertTrue(self.rate_limiter.check_rate_limit("user@example.com", "status", 2, timedelta(minutes=1)))
        self.assertTrue(self.rate_limiter.check_rate_limit("user@example.com", "status", 2, timedelta(minutes=1)))
        self.assertFalse(self.rate_limiter.check_rate_limit("user@example.com", "status", 2, timedelta(minutes=1)))

class TestNotificationService(unittest.TestCase):
    def setUp(self):
        self.service = NotificationService()

    @patch('notification_service.models.EmailNotification.send')
    def test_send_notification_success(self, mock_send):
        result = self.service.send_notification("user@example.com", "status", "Test message")
        self.assertTrue(result)
        mock_send.assert_called_once_with("user@example.com", "Test message")

    @patch('notification_service.models.EmailNotification.send')
    def test_send_notification_rate_limit_exceeded(self, mock_send):
        self.service.send_notification("user@example.com", "status", "Test message 1")
        self.service.send_notification("user@example.com", "status", "Test message 2")
        result = self.service.send_notification("user@example.com", "status", "Test message 3")
        self.assertFalse(result)
        self.assertEqual(mock_send.call_count, 2)

    def test_send_notification_invalid_type(self):
        result = self.service.send_notification("user@example.com", "invalid_type", "Test message")
        self.assertFalse(result)

    @patch('notification_service.models.EmailNotification.send', side_effect=NotificationSendException("user@example.com", "status", "Test error"))
    def test_send_notification_send_error(self, mock_send):
        result = self.service.send_notification("user@example.com", "status", "Test message")
        self.assertFalse(result)
        mock_send.assert_called_once_with("user@example.com", "Test message")

if __name__ == '__main__':
    unittest.main()