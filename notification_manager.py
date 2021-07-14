from twilio.rest import Client

account_sid = "AC5ca982fc60bf3d16b20558fab6908878"
auth_token = "d4c2bdefd333efe5bfdc7efad474096b"


class NotificationManager:

    def __init__(self):
        client = Client(account_sid, auth_token)

    def send_notifications(self, msg):
        message = self.client.messages \
            .create(
            body=msg,
            from_='+15123557994',
            to='+8801943086629'
        )

        print(message.sid)
