from sqlalchemy import create_engine, desc
from sqlalchemy import Column, Integer, String, ForeignKey

from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///students.db')

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'

    student_id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    teacher_id = Column(Integer())



class Teacher(Base):
    __tablename__ = 'teachers'

    teacher_id = Column(Integer(), ForeignKey('student.teacher_id'), primary_key=True )
    first_name = Column(String())
    last_name = Column(String())
