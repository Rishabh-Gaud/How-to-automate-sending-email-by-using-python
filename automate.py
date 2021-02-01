import os
import smtplib
import imghdr
from email.message import EmailMessage
#enter your email address
EMAIL_ADDRESS = 'enter your email'

#enter your email password 
EMAIL_PASSWORD =12345678

#enter mail address which you want to send message

contacts = [ 'mail01@gmail.com', 'mail1@gmail.com', 'mail21@gmail.com']





####################THIS IS YOUR MAIN MASSAGE##########################


for contact in contacts:
    msg = EmailMessage()
    msg['Subject'] = 'HERE IS OUR TITLE'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = contact

    msg.set_content('This is a plain text email')

    msg.add_alternative("""\
    <!DOCTYPE html>
    <html>
        <body>
            <h1 style="color:blue;">This is an HTML Email!</h1>
        </body>
    </html>
    """, subtype='html')

########################################################################



with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)