from django.core.mail import EmailMessage

def send_test_email():
    email = EmailMessage(
        'Subject Here',
        'This is the message body.',
        'tonkungman@gmail.com',
        ['tonkungman@gmail.com']
    )
    email.send()