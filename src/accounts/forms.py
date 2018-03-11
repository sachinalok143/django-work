from django import forms
from .backends import *
from .models import UserProfile
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)

User=get_user_model()

class UserLoginForm(forms.Form):
	email=forms.EmailField()
	password= forms.CharField(widget=forms.PasswordInput)
		
	def clean(self,*args,**kwargs):
		email=self.cleaned_data.get("email")
		password=self.cleaned_data.get("password")
		# user = get_user_model().objects.get(email=email,password)

		user=EmailBackend.authenticate(self,username=email,password=password,**kwargs)
		# user_qs=User.objects.filter(email=email)
		# if user_qs.count()==1:
			# user=user_qs.first()
		if not user:
			raise forms.ValidationError("This User does not exits")
		if not user.check_password(password):
			raise forms.ValidationError("Incorrect Password")
		if not user.is_active:
			raise forms.ValidationError("This User is no longer active")
		return super(UserLoginForm,self).clean(*args,**kwargs)

class UserRegistrationForm(forms.ModelForm):
	password= forms.CharField(widget=forms.PasswordInput,label="Password")
	password2= forms.CharField(widget=forms.PasswordInput,label="Confirm Password")
	email=forms.EmailField(label="Email Address")

	class Meta:
		model=User
		fields=[
		"username",
		"email",
		"first_name",
		"last_name",
		"password",
		]
	def clean_password2(self):
		password=self.cleaned_data.get("password")
		password2=self.cleaned_data.get("password2")
		if password != password2:
			raise forms.ValidationError("Two Password Must Match.")
		return password
	def clean_email(self):
		email=self.cleaned_data.get("email")
		email_qs=User.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError("This email has already been registered.")
		return email


class UserProfileForm(forms.ModelForm):
	class Meta:
		model=UserProfile
		fields=[
		"Address",
		"Phone",
		"A_Value",
		"B_Value",
		"C_Value",
		"D_Value",
		]


	
		