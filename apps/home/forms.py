from django import forms
from apps.home.models import CustomerInfo
import os
from .models import *


class CustomerEditForm(forms.ModelForm):
   class Meta:
      model = CustomerInfo
      fields = '__all__'

   first_name = forms.CharField(
      widget=forms.TextInput(
            attrs={
               "placeholder": "Customer first name",
               "class": "form-control"
            }
      )
   )

   last_name = forms.CharField(
      widget=forms.TextInput(
            attrs={
               "placeholder": "Customer last name",
               "class": "form-control"
            }
      )
   )

   email_address = forms.CharField(
      widget=forms.TextInput(
            attrs={
               "placeholder": "Customer email address",
               "class": "form-control"
            }
      )
   )

   phone_no = forms.CharField(
      widget=forms.TextInput(
            attrs={
               "placeholder": "Customer phone number",
               "class": "form-control"
            }
      )
   )

   address = forms.CharField(
      widget=forms.TextInput(
            attrs={
               "placeholder": "Customer physical address",
               "class": "form-control"
            }
      )
   )
   
   def custFormName(self):
      return os.path.basename(self.CustomerInfo.name)