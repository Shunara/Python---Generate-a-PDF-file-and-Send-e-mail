# Importing the libraries that will be used
from email.message import EmailMessage
import os.path
import mimetypes
import smtplib
import getpass

# Creating an empty message
message = EmailMessage()

# Substitute the sender and recipient values
# with any e-mail(s) of your choice
sender = "me@example.com"
recipient = "you@example.com"
message['From'] = sender
message['To'] = recipient

# Adding a subject to the message
message['Subject'] = 'Using Python to send an e-mail from {} to {}'.format(sender, recipient)

# Editing the body of the e-mail
body = """Hey there! I sent this e-mail to you using Python!"""
message.set_content(body)
print(message)