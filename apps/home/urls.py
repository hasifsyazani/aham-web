from django.urls import path
from apps.home import views
from . import views
from .views import EditCustomer, CustomerList

urlpatterns = [
    path("", views.index, name="home"),
    path("list-customer/", CustomerList.as_view(), name="listcust"),
    path("list-customer/edit-customer/<int:pk>", EditCustomer.as_view(), name="editcust"),
    path('profile/', views.profile, name='profile'),
    path('table/', views.table, name='table'),

]
