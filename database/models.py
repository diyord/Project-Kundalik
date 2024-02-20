from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, Date, DateTime, Float
from sqlalchemy.orm import relationship
from database import Base

class Teacher(Base):
    __tablename__ = 'Teachers'
    name = Column(String)
    surname = Column(String)
    phone_number = Column(Integer, unique=True)
    password = Column(Integer)
    school = Column(Integer)
    teacher_id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True)
    grates = Column(Integer)

class Student(Base):
    __tablename__ = 'Students'
    name = Column(String)
    surname = Column(String)
    password = Column(Integer)
    student_id = Column(Integer, primary_key=True, autoincrement=True)
    phone_number = Column(Integer, unique=True)
    school = Column(Integer)
    email = Column(String)
    grate = Column(Integer)
    word_of_class = Column(String)

class StudentHomework():
    __tablename__ = 'Homework'
    homework_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, primary_key=True, autoincrement=True)
    homework_number = Column(Integer, nullable=False, unique=True)
    done_homework = Column(Integer, default=0)
    exp_date = Column(Integer)
    home_task = Column(String)
    student_fk = relationship(Student, lazy='subquery')

