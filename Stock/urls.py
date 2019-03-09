from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from CroStocks import views
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    path('',views.list_all_stocks,name='all_stocks')
]