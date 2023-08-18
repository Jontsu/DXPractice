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

## Current Application Build
[Current version can be viewed here](https://guarded-taiga-97204-f0af444033df.herokuapp.com)

## TO DO's
- Implement a feature for returning solutions, which includes an input field for GitHub links.
- Develop a peer review system for solutions.
- Create a user statistics feature to track and display user activity.
- Develop a student performance tracking system.
- Implement input verifications for user data, such as ensuring email addresses are in the correct format and passwords meet minimum complexity requirements.
- Improve the styling of the exercise page for better user experience.
- Add an edit functionality for the exercise, but only for the user who created it.

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
