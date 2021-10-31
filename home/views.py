from django.shortcuts import render
import pandas as pd
from .models import *
import datetime
from datetime import timedelta

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
        date_list = pd.date_range(start=startDate, end=endDate)
        deposit_1 = deposit.objects.filter(deposit_account_id=1).filter(created__range=[startDate, endDate])  #삼성증권
        deposit_2 = deposit.objects.filter(deposit_account_id=2).filter(created__range=[startDate, endDate])  # 국민은행 인덱스펀드
        deposit_3 = deposit.objects.filter(deposit_account_id=3).filter(created__range=[startDate, endDate])  # KB증권 미국주식 메인
        deposit_4 = deposit.objects.filter(deposit_account_id=4).filter(created__range=[startDate, endDate])  # 신한금투 미국주식 서브

    else:
        startDate = "None"
        endDate = "None"
        date_list = pd.date_range(start="2020-07-27", end=datetime.date.today())
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

    today = datetime.datetime.today()
    todatStr = today.strftime("%Y년 %m월 %d일")
    today_year = datetime.datetime.today().year
    today_month = datetime.datetime.today().month
    today_day = datetime.datetime.today().day

    asset_1 = asset.objects.filter(asset_account_id=1)  # 삼성증권
    list_asset_1 ={}
    list_asset_1_temp=[-1]
    for d in date_list:
        for a in asset_1:
            if d.strftime("%Y-%m-%d") == a.created.strftime("%Y-%m-%d"):
                list_asset_1[d.strftime("%Y-%m-%d")] = a.current_amount
                list_asset_1_temp = []
                list_asset_1_temp.append(a.current_amount)
            else:
                list_asset_1[d.strftime("%Y-%m-%d")] = list_asset_1_temp[0]
    print(list_asset_1[today.strftime("%Y-%m-%d")])


    i=0
    total_deposit_sum = 0
    total_asset_sum = 0
    for a in accounts:
        dummy=[]
        list_asset_temp = [-1]
        dict_asset = {}
        i+=1
        dummy.append(a)
        if request.method == "POST":
            savings = deposit.objects.filter(deposit_account__ordering_level=i).filter(created__range=[startDate, endDate])
            assets = asset.objects.filter(asset_account__ordering_level=i).filter(created__range=[startDate, endDate])
            dummy.append(savings)
            deposit_sum = 0
            for d in savings:
                deposit_sum += d.inAndOut
                total_deposit_sum += d.inAndOut
            dummy.append(deposit_sum)
            for d in date_list:
                for a in assets:
                    if d.strftime("%Y-%m-%d") == a.created.strftime("%Y-%m-%d"):
                        dict_asset[d.strftime("%Y-%m-%d")] = a.current_amount
                        list_asset_temp = []
                        list_asset_temp.append(a.current_amount)
                    else:
                        dict_asset[d.strftime("%Y-%m-%d")] = list_asset_temp[0]
            dummy.append(dict_asset)
            dummy.append(dict_asset[today.strftime("%Y-%m-%d")])
            total_asset_sum += dict_asset[today.strftime("%Y-%m-%d")]

        else:
            savings = deposit.objects.filter(deposit_account__ordering_level=i)
            assets = asset.objects.filter(asset_account__ordering_level=i)
            dummy.append(savings)
            deposit_sum = 0
            for d in savings:
                deposit_sum += d.inAndOut
                total_deposit_sum += d.inAndOut
            dummy.append(deposit_sum)
            for d in date_list:
                for a in assets:
                    if d.strftime("%Y-%m-%d") == a.created.strftime("%Y-%m-%d"):
                        dict_asset[d.strftime("%Y-%m-%d")] = a.current_amount
                        list_asset_temp = []
                        list_asset_temp.append(a.current_amount)
                    else:
                        dict_asset[d.strftime("%Y-%m-%d")] = list_asset_temp[0]
            dummy.append(dict_asset)
            dummy.append(dict_asset[today.strftime("%Y-%m-%d")])
            total_asset_sum += dict_asset[today.strftime("%Y-%m-%d")]
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
        "today":todatStr,
        "asset_0_today":list_asset_1[today.strftime("%Y-%m-%d")],
        "total_deposit_sum":total_deposit_sum,
        "total_asset_sum":total_asset_sum,
   }

    return render(request, template, context)