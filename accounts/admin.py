from django.contrib import admin
from .models import Account, BerthPlanner, ShippingAgent

# Register your models here.
admin.site.register(Account)
admin.site.register(BerthPlanner)
admin.site.register(ShippingAgent)

