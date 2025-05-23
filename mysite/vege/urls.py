from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('recepies/', recepies ,name='recepies')
]