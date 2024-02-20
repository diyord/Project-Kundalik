from database.models import StudentHomework
from database import get_db

def add_hw_db(homework_id, student_id, home_task):
    db = next(get_db())

    new_homework = StudentHomework(homework_id=homework_id, student_id=student_id, home_task=home_task)

    if new_homework:
        db.add(new_homework)
        db.commit()
    else:
        return 'You do something which come to error'

def exact_student_homework_db(homework_id, student_id):
    db = next(get_db())

    exact_hw = db.query(StudentHomework).filter_by(shomework_id=homework_id, tudent_id=student_id)

    if exact_hw:
        return exact_hw
    else:
        return 'Error, plz try again'

def exact_student_hw_db(student_id, homework_id, done_homework):
    db = next(get_db())

    exact = db.query(StudentHomework).filter_by(student_id=student_id, \
                                                homework_id=homework_id, done_homework=done_homework)

    if exact:
        return exact
    else:
        return 'Error plz try again'

def check_homework_db(homework_number):
    db = next(get_db())

    checker = db.query(StudentHomework).filter_by(homework_number=homework_number)
    if checker:
        return checker
    else:
        return 'Error'

def delete_homework_db(homework_id):
    db = next(get_db())

    delete_homework = db.delete(StudentHomework).filter_by(homework_id=homework_id)

    if delete_homework:
        return 'Homework successfully deleted'
    else:
        return 'Error, try again'

