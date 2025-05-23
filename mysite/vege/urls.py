from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('recepies/', recepies ,name='recepies'),
    path('delete_recepie/<id>/', delete_recepie, name='delete_recepie'),
    path('update_recepie/<id>/', update_recepie, name='update_recepie')
]