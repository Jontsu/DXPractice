CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    github_handle TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL CHECK (role IN ('student', 'teacher'))
);

CREATE TABLE permitted_teachers (
    id SERIAL PRIMARY KEY,
    github_handle TEXT NOT NULL UNIQUE
);

CREATE TABLE permitted_students (
    id SERIAL PRIMARY KEY,
    github_handle TEXT NOT NULL UNIQUE
);

CREATE TABLE exercises (
    id SERIAL PRIMARY KEY,
    creator_id INTEGER REFERENCES users ON DELETE CASCADE,
    name TEXT UNIQUE NOT NULL,
    tasks TEXT NOT NULL
);

CREATE TABLE solutions (
    id SERIAL PRIMARY KEY,
    exercise_id INTEGER REFERENCES exercises ON DELETE CASCADE,
    submitter_id INTEGER REFERENCES users ON DELETE CASCADE,
    solution_link TEXT NOT NULL,
    comment_link_1 TEXT NOT NULL,
    comment_link_2 TEXT NOT NULL,
    comment_link_3 TEXT NOT NULL,
    UNIQUE (submitter_id, exercise_id)
);
