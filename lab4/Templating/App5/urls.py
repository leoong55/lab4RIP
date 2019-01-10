"""Templating URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^function_view/', views.function_view),
    url(r'^class_based_view/', views.ExampleClassBase.as_view()),
    url(r'^example_view/', views.ExampleView.as_view()),
    url(r'^orders_view/', views.OrdersView.as_view()),
    url(r'^empty_orders_view/', views.EmptyOrdersView.as_view()),
    url(r'^order/(?P<id>\d+)', views.OrderView.as_view(), name='order_url'),
]

