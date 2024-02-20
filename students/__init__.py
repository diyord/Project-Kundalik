from pydantic import BaseModel


class StudentRegistrationValidator(BaseModel):
    name: str
    surname: str
    email: str
    phone_number: int
    password: str
    school: str
    classes: str
    grate: int

class EditStudentValidator(BaseModel):
    student_id: int
    edit_date: str
    new_date: str