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
    context = {'recepies' : queryset}

    return render(request,'recepies.html',context)
