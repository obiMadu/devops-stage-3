from flask import Flask, request, jsonify
from tasks import send_email_task, log_time_task
import logging
from logging_config import log_store  # Import log_store to access in-memory logs

app = Flask(__name__)

# Import the logging configuration
import logging_config

@app.route('/')
def index():
    if 'sendmail' in request.args:
        email = request.args.get('sendmail')
        send_email_task.delay(email)
        logging.info(f"Email queued to be sent to {email}")
        return f"Email queued to be sent to {email} \n"
    elif 'talktome' in request.args:
        log_time_task.delay()
        logging.info("Current time logged")
        return "Current time logged.\n"
    return "Welcome to the messaging system!"

@app.route('/log')
def get_log():
    return jsonify(log_store)

if __name__ == '__main__':
    app.run(debug=True)
