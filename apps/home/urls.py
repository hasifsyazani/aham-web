# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('profile/', views.profile, name='profile'),
    path('table/', views.table, name='table'),

]
