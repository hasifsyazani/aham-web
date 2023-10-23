from django import forms
from apps.home.models import CustomerInfo
from django.core.exceptions import ObjectDoesNotExist
from .models import *
import re

class CustomerAddForm(forms.ModelForm):
   class Meta:
      model = CustomerInfo
      fields = '__all__'

   first_name = forms.CharField(
      widget=forms.TextInput(
            attrs={
               "placeholder": "Customer first name",
               "class": "form-control"
            }
      ), required=True
   )

   last_name = forms.CharField(
      widget=forms.TextInput(
            attrs={
               "placeholder": "Customer last name",
               "class": "form-control"
            }
      ), required=True
   )

   email_address = forms.CharField(
      widget=forms.TextInput(
            attrs={
               "placeholder": "Customer email address",
               "class": "form-control"
            }
      ), required=True
   )

   phone_no = forms.CharField(
      widget=forms.TextInput(
            attrs={
               "placeholder": "Customer phone number",
               "class": "form-control"
            }
      ), required=True
   )

   address = forms.CharField(
      widget=forms.TextInput(
            attrs={
               "placeholder": "Customer physical address",
               "class": "form-control"
            }
      ), required=True
   )
   
   def clean(self):
      super(CustomerAddForm, self).clean()
      email_address = self.cleaned_data.get('email_address')
      regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
      
      if not(re.fullmatch(regex, email_address)):
         self._errors['email_address'] = self.error_class(["Email is invalid"])
         
      return self.cleaned_data
   
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
      ), required=True
   )

   last_name = forms.CharField(
      widget=forms.TextInput(
            attrs={
               "placeholder": "Customer last name",
               "class": "form-control"
            }
      ), required=True
   )

   email_address = forms.CharField(
      widget=forms.TextInput(
            attrs={
               "placeholder": "Customer email address",
               "class": "form-control"
            }
      ), required=True
   )

   phone_no = forms.CharField(
      widget=forms.TextInput(
            attrs={
               "placeholder": "Customer phone number",
               "class": "form-control"
            }
      ), required=True
   )

   address = forms.CharField(
      widget=forms.TextInput(
            attrs={
               "placeholder": "Customer physical address",
               "class": "form-control"
            }
      ), required=True
   )
   
   def clean(self):
      super(CustomerEditForm, self).clean()
      email_address = self.cleaned_data.get('email_address')
      regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
      
      if not(re.fullmatch(regex, email_address)):
         self._errors['email_address'] = self.error_class(["Email is invalid"])
         
      return self.cleaned_data