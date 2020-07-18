

from django.db import models

class BalanceSheet(models.Model):
    date = models.CharField(max_length=100)
    total_assets = models.CharField(max_length=100)
    total_liabilities = models.CharField(max_length=100)
    total_equity = models.CharField(max_length=100)
