# from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'home'
urlpatterns = [
    path('', home, name="home"),
    path('home/', home, name="home"),
    path('home/chart-asset/', assetChart, name="chart-asset"),
    path('asset/add/', addAsset.as_view(), name='add-asset'),
    path('asset/detail/<int:id>/', assetDetail, name='detail-asset'),
    path('deposit/add/', addDeposit.as_view(), name='add-deposit'),
]