from database.models import Student
from database import get_db

def registration_student_db(name, surname, password, email, \
                            phone_number, school, grate, word_of_class):
    db = next(get_db())
    new_student = Student(name=name, surname=surname, password=password,\
                          email=email, phone_number=phone_number,\
                          school=school, grate=grate, word_of_class=word_of_class)
    db.add(new_student)
    db.commit()

def get_exact_student_db(student_id):
    db = next(get_db())

    exact_student = db.query(Student).filter_by(student_id=student_id)
    if exact_student:
        return exact_student
    else:
        return 'Error! Student not found, plz try again'

def get_all_students_db():
    db = next(get_db())

    all_students = db.query(Student).all()

    return all_students

def check_student_email(email):
    db = next(get_db())

    check = db.query(Student).filter_by(email=email).first()

    if check:
        return check
    else:
        return 'This email is not exist!'

def edit_student_db(student_id, edit_info, new_info):
    db = next(get_db())

    exact_student = db.query(Student).filter_by(student_id=student_id, edit_info=edit_info, new_info=new_info)

    if exact_student:
        if edit_info == 'name':
            exact_student.name = new_info
        elif edit_info == 'surname':
            exact_student.surname = new_info
        elif edit_info == 'school':
            exact_student.school = new_info
        if edit_info == 'email':
            exact_student.email = new_info
        elif edit_info == 'grate':
            exact_student.grate = new_info
        elif edit_info == 'word_of_class':
            exact_student.word_of_class = new_info
        else:
            return 'Info successfully added!'
    else:
        return 'Error! this function is not exist!! Plz try another function'

def delete_student_db(student_id):
    db = next(get_db())

    student = db.query(Student).filter_by(student_id=student_id).first()

    if not student:
        return 'Student not found((('
    else:
        db.delete(student)
        db.commit()
        return 'Student deleted!'
