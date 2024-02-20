from database import get_db
from database.models import Student, Teacher

def registration_teacher_db(name, surname, password, teacher_id, school):
    db = next(get_db())

    new_teacher =Teacher(name=name, surname=surname, password=password, teacher_id=teacher_id, school=school)

    db.add(new_teacher)
    db.commit()
    return 'successfull'

def get_exact_teacher_db(teacher_id):
    db = next(get_db())

    exact_teacher = db.query(Teacher).filter_by(teacher_id=teacher_id)

    if exact_teacher:
        return exact_teacher
    else:
        return 'Error(, try again'

def get_all_teachers_db():
    db = next(get_db())

    get_all_teachers = db.query(Teacher).all()

    if get_all_teachers:
        return get_all_teachers
    else:
        return 'Error(, try again'

def check_email_teacher_db(email):
    db = next(get_db())

    check = db.query(Student).filter_by(email=email).first()

    if check:
        return check
    else:
        return 'Error, this email not exist'

def edit_teacher_db( teacher_id, new_info, edit_info):
    db = next(get_db())

    edit_teacher = db.query(Student).filter_by(teacher_id=teacher_id, new_info=new_info, edit_info=edit_info)

    if edit_teacher:
        if edit_info == 'name':
            edit_teacher.name = new_info
        elif edit_info == 'surname':
            edit_teacher.surname = new_info
        elif edit_info == 'school':
            edit_teacher.school = new_info
        elif edit_info == 'email':
            edit_teacher.email = new_info
        elif edit_info == 'grate':
            edit_teacher.grate = new_info
        else:
            return 'Information successfully changed!'
    else:
        return 'Error((, try again plz'

def delete_student_db(teacher_id):
    db = next(get_db())

    teacher = db.query(Student).filter_by(teacher_id=teacher_id).first()

    if not teacher:
        return 'Teacher not found((('
    else:
        db.delete(teacher)
        db.commit()
        return 'Teacher deleted!'
