from django.shortcuts import render
from utils.validation_rules import validate_user_email
from djando import forms
# Create your views here.
from rest_framework.generics import ListAPIView
from .models import MenuCategory
from .serializers import MenuCategorySerializer
from rest_framework import generics
from .models import Table
from .serializers import TableSerializer

class RegistrationForm(forms.Form):
    email=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.passwordInput)
    def clean_email(self):
        email_address=self.cleaned_data.get('email')
        if not validate_user_email(email_address):
            raise forms.ValidationError("Please enter a valid email address.")
        return email_address

class TableDetailView(generics.RetrieveAPIView):
    queryset=Table.objects.all()
    serializer_class=TableSerializer