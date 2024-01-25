# Grocery Store

A modern grocery store platform built using Flask and it's extensions for SQLite and REST APIs, along with Vue.js for the frontend. It is built with user experience in mind, with flexibility to visualise and manage finances to the granular level.

## How to run the application
1. Open the terminal at the root folder
2. If there is no folder in the root directory by the name `.env`, create a virtual environment for the project to run in and install the dependencies from `requirements.txt`. The following methods can be used to execute this step:
    - **For *nix system users**, to do it **manually**, execute the following commands in the given order:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
    - **For Windows users**, the setup can be done manually by using the following commands in the given order (**Note**: It is advisable to use WSL with Ubuntu instead of the Windows powershell for Redis and other dependencies of the app):
    ```powershell
    python3 -m venv .venv
    .\.venv\Scripts\activate
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
3. Source the virtual environment in the terminal using either of the following methods:
    - **For *nix system users**, to complete this and the next stworkersep, it can be completed **manually** by running either of the following commands:
        - `source .env/bin/activate`
        - `. .env/bin/activate`
    - **For Windows users**, running the following command in the terminal should suffice: `.env\Scripts\activate`
4. Run the redis server by running the command: `redis-server`. Redis can be downloaded from the following link: [https://redis.io/download/#redis-downloads](https://redis.io/download/#redis-downloads). Since, the redis server will occupy the terminal, open a new tab in the terminal for the subsequent steps.
5. Run the celery worker and beat with the following command: `celery -A main:celery_app worker -l INFO --beat`. Since, the celery process will occupy the terminal, open a new tab in the terminal for the subsequent steps.
7. Optionally, we can use MailHog to test the mails. The configuration inside the app is set for MailHog by default. We can run the program using the following command: `~/go/bin/MailHog`. MailHog needs to be installed in the system before running this command, installation steps can be found here: [https://github.com/mailhog/MailHog?tab=readme-ov-file#installation](https://github.com/mailhog/MailHog?tab=readme-ov-file#installation). Since, MailHog will occupy the terminal, open a new tab in the terminal for the subsequent steps.
8. Run the `main.py` file using the following command: `python3 main.py`
## Technologies used
- Python v3.7.3
    - External dependencies are listed out in `requirements.txt`.
- Redis (`redis-server`)
- HTML5, CSS3, JavaScript (Vue.js)
- Bootstrap v5.0.2

## Folder structure and important files
- `/app/utils/config.py` contains all the configurations / constants required to run the application. Any parameters can be directly changed in this file.
- `main.py` is the main entry point of the app.
- `requirements.txt` contains all the direct / indirect dependencies needed for the application to work.
- `README.md` is literally the file you are reading right now.
- `/.env/` contains the virtual environment for running the application.
- `/app/` contains the main components of the application.
- `/app/controller/` contains the function declarations of various operations performed by the APIs.
- `/app/models/` contains the object models of the various schemas declared in the database.
- `/app/services/` contains the functions of all the celery tasks that the app is required to perform.
- `/app/services/reports/` contains the functions required to generate HTML reports.
- `/app/services/reports/_templates/` contains the HTML templates for the reports.
- `/app/utils/` contains all utility functions and instances required across the app.
- `/app/views/` contains all the routes at which the API endpoints will return data by `flask`.
- `/db/` contains the database used in the project.
- `/docs/` contains the documentation of the API for the application.
- `/static/` contains the static resources like CSS and JS files necessary for functionality of the app. It also contains some media related to the app.
- `/templates/` contains the HTML templates used for rendering HTML on the server.