"""
Problem Statement:
Create a base class Notification with a method send().
Derive EmailNotification, SMSNotification, and PushNotification.
Override send() to display the appropriate notification method.
"""

class Notification:
    def send(self):
        print("Sending notification")


class EmailNotification(Notification):
    def send(self):
        print("Sending Email Notification")


class SMSNotification(Notification):
    def send(self):
        print("Sending SMS Notification")


class PushNotification(Notification):
    def send(self):
        print("Sending Push Notification")


notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]

for notification in notifications:
    notification.send()