import smtplib, time, ssl, datetime
from email.message import EmailMessage

def send_email():
    smtp_server = "smtp.gmail.com"
    port = 587
    
    msg = EmailMessage()
    
    msg["From"] = "your-email@gmail.com"
    msg["To"] = "reciever-email@gmail.com"
    msg["Subject"] = "Spam Subject" 

    msg.set_content("Enter you message here!")

    context =  ssl.create_default_context()
    
    with smtplib.SMTP(smtp_server, port) as server:
    
        server.ehlo()
        server.starttls(context = context)
        server.ehlo()
       
        server.login(msg["From"],"passcode")
    
        print("Logged In")
        
        server.send_message(msg)
        print("Message Sent")

if __name__ == "__main__":
    sent_messages = 1
    start_time = time.time()

    while sent_messages < 150:
        end_time = time.time()
        duration = end_time - start_time

        if duration > 310:
            send_email()
            start_time = end_time
            print(f'Email number {sent_messages} has been sent at {datetime.datetime.now()}')
            sent_messages += 1
