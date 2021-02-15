from django.contrib import admin
from .models import Subscription,MonthlyOrder
from import_export import resources
from import_export.admin import ImportExportModelAdmin

import tablib


# Register your models here.

class SubscriptionResource(resources.ModelResource):
    class Meta:
        model=Subscription
        fields=['id','user__email','active','fulfilled']

class SubscriptionAdmin(ImportExportModelAdmin):
    resource_class = SubscriptionResource
    list_display = ['user','fulfilled','active']
    list_filter = ['active','fulfilled']

class MonthlyOrderResource(resources.ModelResource):
    class Meta:
        model=MonthlyOrder
        fields=['subscription','tracking']

class MonthlyOrderAdmin(ImportExportModelAdmin):
    resource_class = MonthlyOrderResource


admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(MonthlyOrder, MonthlyOrderAdmin)
