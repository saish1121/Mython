import smtplib
import os
from email.message import EmailMessage
import Platform_Surveillance_System
import Thread_process

def Send_Email(file_path):

    sender_email = "bhide340@gmail.com"
    sender_password = "xgqf smmt ytju olco"
    receiver_email = "saishkolhapure49@gmail.com"

    msg = EmailMessage()
    msg["Subject"] = "Platform Surveillance System Report"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    msg.set_content("Please find attached system monitoring report.")

    # Attach file
    with open(file_path, "rb") as f:
        file_data = f.read()
        file_name = os.path.basename(file_path)

    msg.add_attachment(file_data,
                       maintype="application",
                       subtype="octet-stream",
                       filename=file_name)

    # Connect to Gmail server
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)
        server.send_message(msg)

    print("Email sent successfully!")
