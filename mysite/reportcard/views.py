from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import StudentID,Student,SubjectMarks,ReportCard
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

def get_student(request):
    queryset = Student.objects.all()

    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = queryset.filter(
            Q(student_name__icontains = search) |
            Q(department__department__icontains = search) |
            Q(student_id__student_id__icontains = search) |
            Q(student_email__icontains = search)
        )

    paginator = Paginator(queryset,50) #50 Records on 1 page
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)
    return render(request,'reportcard/students.html',{'queryset' : page_obj})

def get_result(request,student_id):
    student = Student.objects.get(student_id__student_id = student_id)

    reportcard = ReportCard.objects.get(student__student_name = student.student_name)
    print(reportcard)
    rank = reportcard.student_rank

    subjectmarks = SubjectMarks.objects.filter(student = student)
    result = True

    for subjectmark in subjectmarks:
        if subjectmark.marks < 35:
            result = False

    return render(request,'reportcard/results.html',{'subjectmakrs' : subjectmarks , 'student' : student , 'result' : result , 'rank' : rank})