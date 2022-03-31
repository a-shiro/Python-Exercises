def get_emails():
    while True:
        email_info = input().split(' ')

        if email_info[0] == 'Stop':
            break

        sender, receiver, content = email_info
        email = Email(sender, receiver, content)
        emails.append(email)


class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


emails = []
get_emails()
email_indices = map(int, input().split(', '))

for i in email_indices:
    emails[i].send()

[print(email.get_info()) for email in emails]


