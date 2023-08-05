from db import db
from models import Exercise

def create_exercise(name, tasks, creator_id):
    new_exercise = Exercise(name=name, tasks=tasks, creator_id=creator_id)
    db.session.add(new_exercise)
    db.session.commit()
    return True

def delete_exercise(exercise_id, creator_id):
    exercise = Exercise.query.get(exercise_id)
    if exercise and exercise.creator_id == creator_id:
        db.session.delete(exercise)
        db.session.commit()
        return True
    return False
