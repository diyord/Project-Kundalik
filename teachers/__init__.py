from pydantic import BaseModel


class TeacherRegistrationValidator(BaseModel):
    name: str
    surname: str
    email: str
    phone_number: int
    password: str
    school: str
    grate: int

class EditStudentValidator(BaseModel):
    teacher_id: int
    edit_date: str
    new_date: str