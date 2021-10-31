from django.shortcuts import render

# Create your views here.
def home(request):
    template = "home/main.html"
    context = {}

    return render(request, template, context)