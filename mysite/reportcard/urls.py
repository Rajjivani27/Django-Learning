from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *
#from vege.views import login_page

urlpatterns = [
    path('students/',get_student,name="get_student"),
    path('result/<student_id>',get_result,name='get_result'),
]