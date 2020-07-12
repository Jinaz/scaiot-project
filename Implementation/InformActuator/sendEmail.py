import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def sendEmail(receiver_email, content, subject="Information from scaiot project",
              sender_email="noreply.scaiot.project@gmail.com",
              password="scaiot2020g07"):
    message = MIMEMultipart()
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email
    message.attach(MIMEText(content, "plain"))

    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

# if __name__ == "__main__":
#    receiver_email = "noreply.scaiot.project@gmail.com"
#
#    sendEmail(receiver_email, "1. asdgasdg\n" + "2. asdgasdg\n")
