import smtplib 
from email.message import EmailMessage

print("WELCOME to to email sending program")
print("enter sender email id:")
email_id=input()
print("enter sender email id's password:")
Password=input()
print("enter sender's name:")
name=input()
print("enter reciver's email id:")
reciver=input()
print("Subject for email:")
subject=input()
print("content for email:")
content=input()

send=smtplib.SMTP("smtp.gmail.com",587) #creating session for gmail
send.starttls() #transport layer

#============================= Plain Message =========================
msg=EmailMessage()
msg["Subject"]=subject
msg["From"]=name
msg["To"]=reciver

msg.set_content(content)

try:
    send.login(email_id,Password)
except smtplib.SMTPAuthenticationError:
        print("password is wrong")