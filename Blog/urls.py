from django.conf.urls import url
from Blog.views import home_blog

urlpatterns=[
    url('',home_blog),
]