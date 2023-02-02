from sqlalchemy import create_engine, desc, Column, Integer, String, DateTime, PrimaryKeyConstraint, UniqueConstraint, CheckConstraint, Index
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
engine = create_engine('sqlite:///migrations_test.db')
Base = declarative_base()

class Student(Base):
    __tablename__ = 'scholars'
    __table_args__ = (
        PrimaryKeyConstraint(
            'id',
            name='id_pk'),
        UniqueConstraint(
            'email',
            name='unique_email'),
        CheckConstraint(
            'grade BETWEEN 1 AND 12',
            name='grade_between_1_and_12'))

    Index('index_name', 'name')

    id = Column(Integer())
    name = Column(String())
    email = Column(String(55))
    grade = Column(Integer())
    birthday_datetime = Column(DateTime())
    enrolled_date = Column(DateTime(), default=datetime.now())

    def __repr__(self):
        return f"Student {self.id}: " \
            + f"{self.name}, " \
            + f"Grade: {self.grade}"