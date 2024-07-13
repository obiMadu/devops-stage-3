Certainly! Here is a GitHub README for your project:

---

# Messaging System with RabbitMQ, Celery, and Flask

This project demonstrates how to deploy a Python application behind Nginx that interacts with RabbitMQ and Celery for email sending and logging functionality.

## Table of Contents

- [Messaging System with RabbitMQ, Celery, and Flask](#messaging-system-with-rabbitmq-celery-and-flask)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Testing](#testing)
  - [Endpoints](#endpoints)
  - [Configuration](#configuration)
  - [License](#license)

## Introduction

This messaging system uses Flask for the web framework, RabbitMQ as the message broker, and Celery for asynchronous task processing. The application includes endpoints to send emails and log the current time. Logs can be accessed via a dedicated `/log` endpoint.

## Features

- Asynchronous email sending using RabbitMQ and Celery
- Logging of current time
- Nginx setup to serve the Flask application
- Endpoint to access logs

## Requirements

- Python 3.8+
- RabbitMQ
- Redis
- Nginx
- `pip` and `virtualenv` for Python package management

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/messaging_system.git
    cd messaging_system
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Install and start RabbitMQ:**
    ```sh
    # For Debian-based systems
    sudo apt-get update
    sudo apt-get install rabbitmq-server
    sudo systemctl start rabbitmq-server

    # For MacOS (using Homebrew)
    brew update
    brew install rabbitmq
    brew services start rabbitmq
    ```

5. **Install and start Redis:**
    ```sh
    # For Debian-based systems
    sudo apt-get update
    sudo apt-get install redis-server
    sudo systemctl start redis-server

    # For MacOS (using Homebrew)
    brew update
    brew install redis
    brew services start redis
    ```

6. **Configure and start Nginx:**
    ```sh
    # Copy nginx.conf to the Nginx configuration directory
    sudo cp nginx.conf /etc/nginx/sites-available/default
    sudo systemctl restart nginx
    ```

## Usage

1. **Start the Celery worker:**
    ```sh
    celery -A celery_worker worker --loglevel=info
    ```

2. **Run the Flask application:**
    ```sh
    sudo -E venv/bin/python app.py
    ```

## Testing

You can test the application using `curl` or any HTTP client:

1. **Test the `sendmail` functionality:**
    ```sh
    curl "http://localhost:5000/?sendmail=example@example.com"
    ```

2. **Test the `talktome` functionality:**
    ```sh
    curl "http://localhost:5000/?talktome"
    ```

3. **View the logs via the `/log` endpoint:**
    ```sh
    curl "http://localhost:5000/log"
    ```

## Endpoints

- `GET /?sendmail=<email>`: Queues an email to be sent to the specified address.
- `GET /?talktome`: Logs the current time.
- `GET /log`: Retrieves all log entries.

## Configuration

- **SMTP Settings:** Configure your SMTP server settings in `smtp_settings.py`.
- **Nginx Configuration:** The Nginx configuration file `nginx.conf` should be adjusted to match your system's setup.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to customize the README to better suit your project's specifics and needs.