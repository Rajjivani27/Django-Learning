from django.db.models import F
from django.db.models import Count
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

def say_hello(request):
    return HttpResponse("Hello! Welcome Here")

