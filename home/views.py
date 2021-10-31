from django.shortcuts import render
from .models import *
import datetime

# Create your views here.
def home(request):
    template = "home/main.html"
    accounts = account.objects.all()
    deposit_1_sum = 0
    deposit_2_sum = 0
    deposit_3_sum = 0
    deposit_4_sum = 0
    data=[]
    if request.method == "POST":
        startDate = request.POST['startDate']
        endDate = request.POST['endDate']
        deposit_1 = deposit.objects.filter(deposit_account_id=1).filter(created__range=[startDate, endDate])  #삼성증권
        deposit_2 = deposit.objects.filter(deposit_account_id=2).filter(created__range=[startDate, endDate])  # 국민은행 인덱스펀드
        deposit_3 = deposit.objects.filter(deposit_account_id=3).filter(created__range=[startDate, endDate])  # KB증권 미국주식 메인
        deposit_4 = deposit.objects.filter(deposit_account_id=4).filter(created__range=[startDate, endDate])  # 신한금투 미국주식 서브

    else:
        startDate = "None"
        endDate = "None"
        deposit_1 = deposit.objects.filter(deposit_account_id=1)  # 삼성증권
        deposit_2 = deposit.objects.filter(deposit_account_id=2)  # 국민은행 인덱스펀드
        deposit_3 = deposit.objects.filter(deposit_account_id=3)  # KB증권 미국주식 메인
        deposit_4 = deposit.objects.filter(deposit_account_id=4)  # 신한금투 미국주식 서브

    for d in deposit_1:
        deposit_1_sum += d.inAndOut
    for d in deposit_2:
        deposit_2_sum += d.inAndOut
    for d in deposit_3:
        deposit_3_sum += d.inAndOut
    for d in deposit_4:
        deposit_4_sum += d.inAndOut

    asset_1 = asset.objects.filter(deposit_account_id=1)  # 삼성증권
    

    i=0
    for a in accounts:
        dummy=[]
        i+=1
        dummy.append(a)
        if request.method == "POST":
            savings = deposit.objects.filter(deposit_account_id=i).filter(created__range=[startDate, endDate])
            dummy.append(savings)
            deposit_sum = 0
            for d in savings:
                deposit_sum += d.inAndOut
            dummy.append(deposit_sum)
        else:
            savings = deposit.objects.filter(deposit_account_id=i)
            dummy.append(savings)
            deposit_sum = 0
            for d in savings:
                deposit_sum += d.inAndOut
            dummy.append(deposit_sum)
        data.append(dummy)



    context = {
        "accounts":accounts,
        "startDate":startDate,
        "endDate":endDate,
        "deposit_0":deposit_1,
        "deposit_1":deposit_2,
        "deposit_2":deposit_3,
        "deposit_3":deposit_4,
        "deposit_0_sum": deposit_1_sum,
        "deposit_1_sum": deposit_2_sum,
        "deposit_2_sum": deposit_3_sum,
        "deposit_3_sum": deposit_4_sum,
        "data":data,
   }

    return render(request, template, context)