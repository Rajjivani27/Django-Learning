from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# takes request and returns a response
# its a request handler

def say_hello(request):
    peoples = [
        {'name' : 'Raj Jivani' , 'age' : 17},
        {'name' : 'Dhruvin Andhariya' , 'age' : 22},
        {'name' : 'Jay Kanani' , 'age' : 19},
        {'name' : 'Preet Jani' , 'age' : 19},
        {'name' : 'Raj Modi' , 'age' : 19},
        {'name' : 'Manthan Gajjar' , 'age' : 19}
    ]

    return render(request,'hello.html',context = {'peoples' : peoples})


