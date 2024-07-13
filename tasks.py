from celery import Celery
from smtp_details import SMTP_SERVER, SMTP_USERNAME, SMTP_PORT, SMTP_PASSWORD
import smtplib
from email.mime.text import MIMEText
import datetime
import logging

# create a celery worker
celery = Celery('tasks', broker='redis://localhost:6379/0')

@celery.task
def send_email_task(email):

    try: 
        msg = MIMEText("This is test email from Obi.M - Hngxi Devops track, stage 3.")
        msg['Subject'] = 'Devops stage3 Email from Obi.M'
        msg['From'] = SMTP_USERNAME
        msg['To'] = email

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(SMTP_USERNAME, [email], msg.as_string())
        logging.info(f"Email sent to {email}")

    except Exception as e:
        logging.error(f"Failed to send email to {email}: {e}")

@celery.task
def log_time_task():
    current_time = datetime.datetime.now()
    try:
        with open('/var/log/messaging_system.log', 'a') as log_file:
            log_file.write(f"{current_time}\n")
        logging.info(f"Current time: {current_time}\n")
        logging.info(f"Logged current time: {current_time} \n")
    except Exception as e:
        logging.error(f"Failed to log time: {e}")