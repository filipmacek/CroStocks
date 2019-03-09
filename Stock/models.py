from django.db import models
from CroStocks import settings
# Create your models here.
class Stock(models.Model):
    ticker=models.CharField(max_length=5)
    company=models.TextField(max_length=70)
    isin=models.TextField(max_length=30,default="")
    num_stocks=models.IntegerField()
    nominal=models.TextField()
    issuance_date=models.TextField(max_length=20,default="")
    url=models.TextField(max_length=60,default="")

    def __str__(self):
        return self.ticker
