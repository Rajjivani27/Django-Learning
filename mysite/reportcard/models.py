from django.db import models

class StudentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted = False)

class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department
    
    class Meta:
        ordering = ['department']

class StudentID(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.student_id
    
    class Meta:
        ordering = ['student_id']
    
class Student(models.Model):
    department = models.ForeignKey(Department,related_name="depart",on_delete=models.CASCADE)
    student_id = models.OneToOneField(StudentID,related_name="studentid",on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_email = models.CharField(max_length=100)
    student_age = models.IntegerField(default=18)
    student_address = models.TextField()
    is_deleted = models.BooleanField(default= False)

    objects = StudentManager()
    admin_objects = models.Manager()

    def __str__(self) -> str:
        return self.student_name
    
    class Meta:
        ordering = ['student_name']
        verbose_name = "student"

class Subject(models.Model):
    subject_name = models.CharField(max_length=50)

    def __str__(self)->str:
        return self.subject_name

class SubjectMarks(models.Model):
    student = models.ForeignKey(Student,related_name="studentmarks",on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,related_name="subjectmarks",on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.student.student_name}  {self.subject.subject_name}'

    class Meta:
        unique_together = ['student','subject']

class ReportCard(models.Model):
    student = models.ForeignKey(Student,related_name="studentreportcard",on_delete=models.CASCADE)
    student_rank = models.IntegerField()
    date_of_report_generations = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.student} {self.student_rank}'

