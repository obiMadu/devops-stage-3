from flask import Flask, request, jsonify
from tasks import send_email_task, log_time_task
import logging
import os

app = Flask(__name__)

# Set up logging
log_file = './messaging_system.log'
logging.basicConfig(filename=log_file, level=logging.INFO, 
                    format='%(asctime)s %(levelname)s %(message)s')

# Create an in-memory log store
log_store = []

class InMemoryHandler(logging.Handler):
    def emit(self, record):
        log_store.append(self.format(record))

# Add the in-memory handler to the logger
in_memory_handler = InMemoryHandler()
in_memory_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
logging.getLogger().addHandler(in_memory_handler)

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
