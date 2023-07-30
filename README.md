# DXPractice
Simple tool to improve and practice developer experience (DX). 

Teachers can create exercises in the tool, which consist of different coding tasks. Each task requires a solution code (in any language) that relates to a specific topic.

## Features of the tool include:

- **Account Management:** Students and teachers can log in and out, as well as create a new account.
- **Exercise Catalog:** Users can view a list of the available exercises in the tool and can access information about each exercise.
- **Coding Practice:** Students can practice their coding skills by providing solutions to the tasks in the exercise. On each task, the student will write code for a randomly selected topic, which will then be submitted for review.
- **Peer Review:** The solutions provided by students are graded and reviewed by their peers. Each solution must receive a minimum of three reviews by other students before a grade is assigned, enhancing the student's learning and understanding through peer evaluation.
- **User Statistics:** Students can see statistics from each exercise, such as the number of tasks they have attempted and the feedback on their solutions, along with their grades based on the peer reviews.
- **Exercise Creation (Teachers only):** Only teachers can create a new exercise by providing the name of the exercise and a list of tasks in text format.
- **Exercise Deletion (Teachers only):** Teachers can delete exercises that they have created.
- **Access Student Performance (Teachers only):** Teachers can access statistics that show the performance of each student on every exercise they have created, including the grades they have received based on peer reviews.

## Developing

Add .env file into the root of the project with the following lines providing your secret key and your project folder root between sqlite:/// and /database.db so that SQLite can create a dev environment database

.env
```bash
SECRET_KEY=your-secret-key
SQLALCHEMY_DATABASE_URI=sqlite:///[path/to/your/project/directory]/database.db
```

secret key can be generated with Python interpreter by running command 'python' or 'python3' in your terminal and typing the following

```bash
import os
print(os.urandom(24))
```
