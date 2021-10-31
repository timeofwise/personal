from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    template = "home/main.html"
    accounts = account.objects.all()
    deposit_1 = deposit.objects.filter(deposit_account_id=1) #삼성증권
    len_accounts = len(accounts)


    context = {
        "accounts":len_accounts,
        "deposit_1":deposit_1,
   }

    return render(request, template, context)