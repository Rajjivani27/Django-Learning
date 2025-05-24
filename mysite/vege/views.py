from django.shortcuts import render,redirect
from .models import *

# Create your views here.
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

def delete_recepie(request,id):
    queryset = Recepie.objects.get(id = id)
    queryset.delete()
    return redirect('/recepies/')

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

