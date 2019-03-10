from django.shortcuts import render
from Stock.models import Stock

# Create your views here.

def list_all_stocks(request):
    stocks=Stock.objects.all()
    return render(request,'stock_list.html',{'stocks':stocks})

