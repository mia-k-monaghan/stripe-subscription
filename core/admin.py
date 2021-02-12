from django.contrib import admin
from .models import Subscription
from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Register your models here.

class SubscriptionResource(resources.ModelResource):
    class Meta:
        model=Subscription
        fields=('user','active','tracking')

class SubscriptionAdmin(ImportExportModelAdmin):
    resource_class = SubscriptionResource

admin.site.register(Subscription, SubscriptionAdmin)
