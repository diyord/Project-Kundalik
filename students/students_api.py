from fastapi import APIRouter
from database.student_servise import get_all_students_db, edit_student_db, \
    check_student_email, get_exact_student_db, registration_student_db, delete_student_db
from datetime import datetime
from students import StudentRegistrationValidator, EditStudentValidator

student_router = APIRouter(prefix='/student', tags=['Student'])

@student_router.post('/register')
async def register_new_student(data:StudentRegistrationValidator):
    new_student_data = data.model_dump()

    checker = check_student_email(data.email)

    if checker:
        return {'message': 'Student successfully registed'}
    else:
        result = registration_student_db(reg_date=datetime.now(), **new_student_data)

        return result
@student_router.get('/get-student')
async def get_student(student_id: int):

    result = get_exact_student_db(student_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Student not found('}

@student_router.post('/edit')
async def edit_student(data:EditStudentValidator):
    change_data = data.model_dump()

    result = edit_student_db(**change_data)
    return result

@student_router.get('/all-students')
async def get_all_users():

    all_students = get_all_students_db()

    if all_students:
        return {'message': all_students}
    else:
        return {'message': 'This student is not exist'}

@student_router.delete('/delete_users')
async def delete_all_users(user_id: int):
    del_user = delete_student_db(user_id)

    if del_user:
        return {'message': 'Student successfully deleted'}
    else:
        return {'message': 'This student is not exist'}
