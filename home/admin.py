from django.contrib import admin
from .models import *

# Register your models here.

class accountAdmin(admin.ModelAdmin):
    list_display = ['id', 'account_name']

admin.site.register(account, accountAdmin)

class depositAdmin(admin.ModelAdmin):
    list_display = ['id', 'index', 'amount', 'deposit_account', 'created']
    #list_editable = ['created']

admin.site.register(deposit, depositAdmin)

class assetAdmin(admin.ModelAdmin):
    list_display = ['id', 'current_amount']
    ordering = ['-created']

admin.site.register(asset, assetAdmin)

class dataAdmin(admin.ModelAdmin):
    list_display = ['id', 'created']
    ordering = ['-created']

admin.site.register(data, dataAdmin)

