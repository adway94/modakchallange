from notification_service.services import NotificationService

def main():
    service = NotificationService()
    
    # Test successful send
    service.send_notification("user@example.com", "status", "Status update")
    
    # Test rate limit exceeded
    service.send_notification("user@example.com", "status", "Another status update")
    service.send_notification("user@example.com", "status", "Third status update")
    
    # Test invalid notification type
    service.send_notification("user@example.com", "invalid_type", "Invalid content")
    
    # Test send error
    service.send_notification("invalid_user@example.com", "news", "Daily news")

if __name__ == "__main__":
    main()