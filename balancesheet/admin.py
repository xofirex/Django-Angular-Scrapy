from django.contrib import admin
from .models import BalanceSheet

class BalanceSheetAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BalanceSheet._meta.fields]

    class Meta:
        model = BalanceSheet


admin.site.register(BalanceSheet, BalanceSheetAdmin)