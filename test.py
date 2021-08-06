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
# Be aware about this: You must configurate your e-mail before using this program.
sender = "leonardodealbuquerque2@gmail.com"
recipient = "leonardodealbuquerque2@gmail.com"
message['From'] = sender
message['To'] = recipient

# Adding a subject to the message
message['Subject'] = 'Using Python to send an e-mail from {} to {}'.format(sender, recipient)

# Editing the body of the e-mail
body = """Hey there! I sent this e-mail to you using Python!"""
message.set_content(body)

# Attaching a Pikachu image to the e-mail
# You can use whatever image you want
#############################################
""" os.getcwd() is the directory where you're executing the code
	make sure the Image directory is inside that directory"""
attachment_path = os.getcwd()+"\\Image\\Pikachu.jpg"
attachment_filename = os.path.basename(attachment_path)
mime_type, _ = mimetypes.guess_type(attachment_path)
mime_type, mime_subtype = mime_type.split('/', 1)

# Finally attaching the image to the e-mail
with open(attachment_path, 'rb') as ap:
	message.add_attachment(ap.read(),
		maintype=mime_type,
		subtype=mime_subtype,
        filename=os.path.basename(attachment_path))

mail_server = smtplib.SMTP_SSL('smtp.gmail.com',1129)
mail_pass = getpass.getpass('Password? ')
mail_server.login(sender, mail_pass)
#print(mail_server.login(sender, mail_pass))