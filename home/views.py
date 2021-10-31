from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    template = "home/main.html"
    accounts = account.objects.all()


    context = {"accounts":accounts}

    return render(request, template, context)