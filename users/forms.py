#Forms
from django import forms
from django.contrib.auth.models import User
from users.models import Profile


class SignupForm(forms.Form):
  username = forms.CharField(
    min_length=3, 
    max_length=30,
    widget=forms.TextInput(attrs={
      'placeholder':'Username',
      'class': 'form-control',
      'required': True
    }))
  password = forms.CharField(
    min_length=10, 
    widget= forms.PasswordInput(attrs={
      'placeholder': 'Password',
      'class':'form-control',
      'required': True
    })
  )
  password_confirmation = forms.CharField(
    min_length=10, 
    widget= forms.PasswordInput(attrs={
      'placeholder': 'Password Confirmation',
      'class':'form-control',
      'required': True
    }))
  first_name = forms.CharField(
    min_length=3,
    max_length=20,
    widget=forms.TextInput(attrs={
      'placeholder':'First Name',
      'class':'form-control',
      'required': True
    })
  )
  last_name = forms.CharField(
    min_length=3,
    max_length=20,
    widget=forms.TextInput(attrs={
      'placeholder':'Last Name',
      'class':'form-control',
      'required': True
    })
  )
  email = forms.CharField(
    min_length=3,
    max_length=20,
    widget=forms.EmailInput(attrs={
      'placeholder':'Email',
      'class':'form-control',
      'required': True
    })
  )

  #Validacion de Username
  def clean_username(self):
    #Username must be unique
    username = self.cleaned_data['username']
    user_in_db = User.objects.filter(username = username).exists()

    if user_in_db:
      raise forms.ValidationError('Username is already taken')
    return username

  def clean(self):
    #Verify passwords match

    data = super().clean()
    password = data['password']
    password_confirmation = data['password_confirmation']
    if password != password_confirmation:
      raise forms.ValidationError("Passwords don't match")
    return data

  def save(self):
    data = self.cleaned_data
    data.pop('password_confirmation')
    user = User.objects.create_user(**data)
    profile = Profile(user=user)
    profile.save()
