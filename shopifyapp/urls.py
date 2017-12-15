from django.conf.urls import url, include
from django.contrib import admin
from shopifyapp import views

urlpatterns = [
    url(r'^view/$', views.ExampleView.as_view())
]
