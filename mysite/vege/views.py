from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not(User.objects.filter(username=username).exists()):
            messages.error(request,'Invalid Username')
            return redirect('/login/')

        user = authenticate(request,username=username,password=password)

        if user is None:
            messages.error(request,'Invalid Password!!')
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/recepies/')
    
    return render(request,'login.html')

def register_page(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.error(request,'Username already exist!!!')
            return redirect('/register/')
        

        user = User.objects.create(
            username = username,
        )


        user.set_password(password)
        user.save()
        
        messages.success(request,'Account Created Succesfully!')
        return redirect('/recepies/')
    
    return render(request,'register.html')

@login_required(login_url='/login/')
def recepies(request):
    if request.method == "POST":
        data = request.POST
        recepie_name = data.get('recepie_name')
        recepie_desc = data.get('recepie_description')
        recepie_image = request.FILES.get('recepie_image')

        print(recepie_name)
        print(recepie_desc)
        print(recepie_image)

        Recepie.objects.create(
            recepie_name = recepie_name,
            recepie_description = recepie_desc,
            recepie_image = recepie_image
        )

        return redirect('/recepies/')
    
    queryset = Recepie.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(recepie_name__icontains = request.GET.get('search'))
    
    context = {'recepies' : queryset}

    return render(request,'recepies.html',context)

@login_required(login_url='/login/')
def delete_recepie(request,id):
    queryset = Recepie.objects.get(id = id)
    queryset.delete()
    return redirect('/recepies/')

@login_required(login_url='/login/')
def update_recepie(request,id):
    recepie = Recepie.objects.get(id = id)
    context = {'recepie' : recepie}

    if request.method == "POST":
        data = request.POST
        if(data.get('recepie_name') != ''): 
            recepie.recepie_name = data.get('recepie_name')
        if(data.get('recepie_description') != ''):
            recepie.recepie_description = data.get('recepie_description')
        if(request.FILES.get('recepie_image') != None):
            recepie.recepie_image = request.FILES.get('recepie_image')

        recepie.save()

        return redirect('/recepies/')
    
    return render(request,'recepie_update.html',context)

def logoutView(request):
    logout(request)
    return redirect('/login/')

