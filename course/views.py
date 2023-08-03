from django.views.generic import ListView
from django.shortcuts import render

from .models import *




def index(request):

    model = Course.objects.all()
    
    context = {
        'model': model,
    }
    
    return render(request, 'index.html',context)