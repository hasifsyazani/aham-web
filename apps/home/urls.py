# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from . import views
from .views import Index, EditCustomer

urlpatterns = [
    path("", Index.as_view(), name="home"),
    path("edit-customer/<int:pk>", EditCustomer.as_view(), name="editcust"),
    path('profile/', views.profile, name='profile'),
    path('table/', views.table, name='table'),

]
