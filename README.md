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
[Current version can be viewed here](https://guarded-taiga-97204-f0af444033df.herokuapp.com)

## TO DO's
- User page, for students it displays their tasks (exercises with missing solutions), for teachers it displays all the students and whether they have completed all their tasks
- Refactor code more readable
- Create finalised styling

## Developing

Create a .env file in the root directory of the project and add the following line, replacing your-secret-key with your actual secret key:

.env
```bash
SECRET_KEY=your-secret-key
```

You can generate a secret key using Python. Open the Python interpreter by typing python or python3 in your terminal, then enter the following commands:

```bash
import os
print(os.urandom(24))
```

To install the necessary dependencies and start the development server, execute the following commands in your terminal. Make sure you are in the root directory of the application:

```bash
pip install -r requirements.txt
flask run
```
