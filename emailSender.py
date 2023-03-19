import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl

#1. I started with importing the smptlib the library, I'm assuming that it will get us the access to the email.
#2. Then imported mime, with which we'll be able to send the text.
#3. Then imported ssl, for the security.
#4. After the transportation of modules, denoting email, subject and body was pretty simple.
#5. to generate password I got it through the securtiy of Gmail, I think it is an enabler, so that we can 
# use gmail as a platform.
#6. After that ataching it with mime, I didn't get that why we need to atach the mime part if we are using smptlib
#7.The smptlib part was pretty understandable, but had a question that why we need to put the email of smptlib below.
#8. It took lesser time than I thought, I got it that we need to import a lib and with the help of it we can send the mail, 
#But the mime part was a bit confusing.


sender_email = "lysingh24@gmail.com"
receiver_email = "receiver@gmail.com"
password = "password-generated-now-deleted"
subject = "A mail from Yuvraj's Bot"
body = """Dear Receiver,

I am Yuvraj's Robot Assistant, and I am reaching out to you today to send a message of well-being on behalf of Yuvraj. Yuvraj wanted to let you know that he is thinking of you and hopes that you are doing well.

As an AI assistant, I don't have the ability to experience emotions, but I understand how important it is to stay connected with those who matter most to us. I hope this message finds you in good health and high spirits.

Please let us know if there is anything we can do to assist you. Yuvraj values your friendship and appreciates your presence in his life.

Thank you for taking the time to read this message, and I hope you have a wonderful day!

Best regards,

Yuvraj's Robot Assistant"""


message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject


message.attach(MIMEText(body, "plain"))

context = ssl.create_default_context()

try:
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
except Exception as e:
    print(e)
finally:
    server.quit()