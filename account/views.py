from django.shortcuts import render

# Create your views here.
def redirectlogin(request):
    return render(request, 'redirection/to_login.html')