from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    template = "home/main.html"
    accounts = account.objects.all()
    deposit_1 = deposit.objects.filter(deposit_account_id=1) #삼성증권
    deposit_2 = deposit.objects.filter(deposit_account_id=2)  # 국민은행 인덱스펀드
    deposit_3 = deposit.objects.filter(deposit_account_id=3)  # KB증권 미국주식 메인
    deposit_4 = deposit.objects.filter(deposit_account_id=4)  # 신한금투 미국주식 서브
    len_accounts = len(accounts)


    context = {
        "accounts":accounts,
        "deposit_1":deposit_1,
        "deposit_2":deposit_2,
        "deposit_3":deposit_3,
        "deposit_4":deposit_4,
   }

    return render(request, template, context)