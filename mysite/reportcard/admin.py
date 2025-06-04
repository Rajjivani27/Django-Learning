from django.contrib import admin
from .models import *

admin.site.register(Department)
admin.site.register(StudentID)

class StudentAdmin(admin.ModelAdmin):
    ordering = ['student_id']
    list_display = ['student_name' , 'student_id']

admin.site.register(Student,StudentAdmin)
admin.site.register(Subject)

class SubjectMarksAdmin(admin.ModelAdmin):
    list_display = ['student','subject','marks']

admin.site.register(SubjectMarks , SubjectMarksAdmin)

class ReportCardAdmin(admin.ModelAdmin):
    list_display = ['student','student_rank','date_of_report_generations']
    ordering = ['student_rank']

admin.site.register(ReportCard,ReportCardAdmin)
