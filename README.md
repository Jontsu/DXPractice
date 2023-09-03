# DXPractice
Simple tool to improve and practice developer experience (DX). 

Teachers can create exercises in the tool, which consist of different coding tasks. Each task requires a solution code (in any language) that relates to a specific topic.

## Features of the tool include:

- **Account Management:** Students and teachers can log in and out, as well as create a new account.
- **Exercise Catalog:** Users can view a list of the available exercises in the tool and can access information about each exercise.
- **Coding Practice:** Students can practice their coding skills by providing solutions to the tasks in the exercise. Solutions are managed via GitHub, either by establishing a new repository or generating an issue within an existing repository. The solution's GitHub link is provided to the tool.
- **Peer Review:** The solutions submitted by students are reviewed by other students. Reviews are submitted as issues within GitHub. The review's GitHub link is provided to the tool.
- **User Statistics:** Students can track which tasks they not completed yet through their profile page.
- **Exercise Creation (Teachers only):** Only teachers can create a new exercise by providing the name of the exercise and a list of tasks in text format.
- **Exercise Deletion or Edit (Teachers only):** Teachers can delete or edit exercises they have created.
- **Access Student Performance (Teachers only):** Teachers can monitor through their profile page which tasks their students have completed or not completed.

## Current Application Build
The free plans for Heroku Postgres have been retired and so there is no deployed application build available. Please refer to Testing & Developing to test the application.

## Testing & Developing

Create a .env file in the root directory of the project and add your secret key and your local database uri:

.env
```bash
SECRET_KEY=your-secret-key
SQLALCHEMY_DATABASE_URI='your-local-database-uri'
```

You can generate a secret key using Python. Open the Python interpreter by typing python or python3 in your terminal, then enter the following commands:

```bash
import os
print(os.urandom(24))
```

It is probably a good idea to create a virtual environment prior to installing dependencies or running the application, so execute the following commands:

```bash
python3 -m venv venv
source venv/bin/activate
```

To install the necessary dependencies and start the development server, execute the following commands in your terminal. Make sure you are in the root directory of the application:

```bash
pip install -r requirements.txt
flask run
```
Database tables are created automatically or you can also write psql < schema.sql at the root folder should you prefer.


Lessons:
- Clean code principles (read the Clean code book table of contents for the exercise structure)
- Identify any areas where the naming convention is unclear and you are not sure what the particular area of the code does
- Identify any if statments that are hard to follow (e.g. nested if statements that do not follow negative cases first principe).
- Identify any areas where do not repeat yourself is not implemented


Refactor css file based on Tailwind's documentation (or youtube info, e.g. corners class, etc)