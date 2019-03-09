from django.core.management.base import BaseCommand
import os
import csv
from Stock import models

def findnth(string, substring, n):
    parts = string.split(substring, n + 1)
    if len(parts) <= n + 1:
        return -1
    return len(string) - len(parts[-1]) - len(substring)

class Command(BaseCommand):
    help='Import list of all companies and their stock data'


    def handle(self, *args, **options):
        self.stdout.write("Importing data")
        x = 'Stock/fixtures/AllCompanies.csv'
        with open(x,'r',encoding='utf8') as f:
            data=csv.DictReader(f)
            for row in data:
                lis=list(row.items())
                # date=lis[5][1]
                # day=date[0:findnth(date,'.',0)]
                # month=date[(findnth(date,'.',0)+1):findnth(date,'.',1)]
                # year=date[(findnth(date,'.',1)+1):]

                models.Stock.objects.create(ticker=row['Simbol'],
                                            company=row['Izdavatelj'],
                                            isin=row['ISIN'],
                                            num_stocks=row['Broj izdanih'].replace('.',''),
                                            nominal=row['Nominala'],
                                            issuance_date=lis[5][1],
                                            url=row['url'])


