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
      ), required=True, help_text='eg: test@gmail.com, test@outlook.com'
   )

   phone_no = forms.CharField(
      widget=forms.TextInput(
            attrs={
               "placeholder": "Customer phone number",
               "class": "form-control"
            }
      ), required=True, help_text='eg: +60123456789, 012-3456789, 0123456789'
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
      phone_no = self.cleaned_data.get('phone_no')
      regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
      regex_phone = r'^(?:[+]6)?0(([0-9]{2}((\s[0-9]{3,4}\s[0-9]{4})|(-[0-9]{3,4}\s[0-9]{4})|(-[0-9]{7,8})))|([0-9]{9,10}))$'
      
      if not(re.fullmatch(regex_email, email_address)):
         self._errors['email_address'] = self.error_class(["Email is invalid"])

      if not(re.fullmatch(regex_phone, phone_no)):
         self._errors['phone_no'] = self.error_class(["Phone number is invalid"])
         
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
      ), required=True, help_text='eg: test@gmail.com, test@outlook.com'
   )

   phone_no = forms.CharField(
      widget=forms.TextInput(
            attrs={
               "placeholder": "Customer phone number",
               "class": "form-control"
            }
      ), required=True, help_text='eg: +60123456789, 012-3456789, 0123456789'
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
      phone_no = self.cleaned_data.get('phone_no')
      regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
      regex_phone = r'^(?:[+]6)?0(([0-9]{2}((\s[0-9]{3,4}\s[0-9]{4})|(-[0-9]{3,4}\s[0-9]{4})|(-[0-9]{7,8})))|([0-9]{9,10}))$'
      
      if not(re.fullmatch(regex_email, email_address)):
         self._errors['email_address'] = self.error_class(["Email is invalid"])

      if not(re.fullmatch(regex_phone, phone_no)):
         self._errors['phone_no'] = self.error_class(["Phone number is invalid"])
         
      return self.cleaned_data