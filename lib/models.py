from datetime import datetime

from sqlalchemy import create_engine, desc
from sqlalchemy import Column, DateTime, Integer, String

from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///students.db')

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'

    student_id = Column(Integer(), primary_key=True)


class Teacher(Base):
    __tablename__ = 'teachers'
