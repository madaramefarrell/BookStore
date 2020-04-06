from django.contrib import admin
from .models import CustomerUser, VendorUser, Market


# Register your models here.

@admin.register(CustomerUser)
class CustomerUserAdmin(admin.ModelAdmin):
    pass


@admin.register(VendorUser)
class VendorUserAdmin(admin.ModelAdmin):
    pass


@admin.register(Market)
class MarketAdmin(admin.ModelAdmin):
    pass
