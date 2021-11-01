# from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'home'
urlpatterns = [
    path('', home, name="home"),
    path('home/', home, name="home"),
    path('home/chart-asset/', assetChart, name="chart-asset"),
    path('add-asset/', addAsset.as_view(), name='add-asset'),
    path('add-deposit/', addDeposit.as_view(), name='add-deposit'),
]