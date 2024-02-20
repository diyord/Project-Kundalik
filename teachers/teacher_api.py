from fastapi import APIRouter
from database.student_servise import registration_student_db, edit_student_db,\
    delete_student_db, get_exact_student_db, get_all_students_db, check_student_email
from datetime import datetime
from database.teacher_servise import registration_teacher_db, edit_teacher_db,\
    get_all_teachers_db, get_exact_teacher_db, check_email_teacher_db
from teachers import TeacherRegistrationValidator, EditStudentValidator

teacher_router = APIRouter(prefix='/teacher', tags=['Teachers'])

@teacher_router.post('/register')
async def register_new_teacher(data:TeacherRegistrationValidator):
    new_teacher_data = data.model_dump()

    checker = check_email_teacher_db(data.email)

    if checker:
        return {'message': 'Teacher with this email is allready exist!'}
    else:
        result = registration_teacher_db(reg_date=datetime.now(), **new_teacher_data)

        return result
@teacher_router.get('/get-teacher')
async def get_teacher(teacher_id: int):
    result = get_exact_teacher_db(teacher_id)
    if result:
        return {'message': result}
    else:
        return {'message': 'Teacher not found((('}

@teacher_router.post('/edit')
async def edit_teacher(data:EditStudentValidator):
    change_data = data.model_dump()

    result = edit_teacher_db(**change_data)
    return result

@teacher_router.get('/all-teachers')
async def delete_all_teachers():
    all_teachers = get_all_teachers_db()
    if all_teachers:
        return {'message': all_teachers}
    else:
        return {'message': 'This teacher is not exist'}

@teacher_router.delete('/delete-teacher')
async def delete_all_teachers(teacher_id:int):
    del_teacher = delete_all_teachers(teacher_id)

    if del_teacher:
        return {'message': 'Teacher successfully deleted'}
    else:
        return {'message': 'This teacher is not exist('}
