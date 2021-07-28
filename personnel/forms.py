from django import forms
from django.contrib.auth.forms import UserCreationForm

from personnel.models import User


# class SignUpForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'ID_number', 'email', 'password1', 'password2', 'gender', 'phone', 'birthday']
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         if commit:
#             user.save()
#         return user
