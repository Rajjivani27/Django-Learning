from faker import Faker
import random
from .models import *

fake = Faker()

def create_subject_marks() -> None:
    try:
        students = Student.objects.all()
        for student in students:
            subjects = Subject.objects.all()
            for subject in subjects:
                SubjectMarks.objects.create(
                    student = student,
                    subject = subject,
                    marks = random.randint(0,100)
                )
    except Exception as e:
        print(e)

def seed_db(n=100) -> None:
    try:
        departments_obj = Department.objects.all()
        studentids = random.sample(range(100,300),n)
        
        for i in range(n):
            random_index = random.randint(0 , len(departments_obj)-1)

            department = departments_obj[random_index]
            student_id = f'STU-{studentids[i]}'
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(20,30)
            student_address = fake.address()

            studentid_obj = StudentID.objects.create(student_id = student_id)

            student = Student.objects.create(
                department = department,
                student_id = studentid_obj,
                student_name = student_name,
                student_email = student_email,
                student_age = student_age,
                student_address = student_address
            )
    except Exception as e:
        print(e)

from django.db.models import Sum

def get_reportcard():
    deps = Department.objects.all()

    for dep in deps:
        ranks = Student.objects.filter(department = dep).annotate(marks = Sum('studentmarks__marks')).order_by('-marks','student_name')

        i = 1

        for rank in ranks:
            ReportCard.objects.create(
                student = rank,
                student_rank = i
            )
            i = i + 1
            
