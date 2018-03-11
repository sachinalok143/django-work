from django.shortcuts import render
from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from .backends import *
from .models import UserProfile
# from .forms import UserLoginForm
# User=User.objects.filter()
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)
title="You are loged in!"
# Create your views here.
def login_view(request):
	A=False
	B=False
	C=False
	D=False
	title="You are loged in!"
	form=UserLoginForm(request.POST or None)
	if form.is_valid():
		email=form.cleaned_data.get("email")
		password=form.cleaned_data.get("password")
		user=authenticate(username=email,password=password)
		login(request,user)
		# print(request.user.is_authenticated())
		# logedInUserProfile=UserProfile.objects.filter(user_=)
		# title=''
		# new_userProfile.save()
	if request.user.is_authenticated():
		logedInUserProfile=UserProfile.objects.get(user_id=request.user.id)
		if logedInUserProfile.A_Value:
			# title+="You are A type user.\n"
			A=True
		if logedInUserProfile.B_Value:
			# title+="You are B type user.\n"
			B=True
		if logedInUserProfile.C_Value:
			C=True
			# title+="You are C type user.\n"
		if logedInUserProfile.D_Value:
			D=True
				# title+="You are D type user.\n"
		return render(request,"form.html",{"title":title,"A":A,"B":B,"C":C,"D":D})

		
	return render(request,"form.html",{"form":form,"submit":"submit","title":title})

def logout_view(request):
	return render(request,"form.html",{})

def register_view(request):
	# title="Register"
	title="You are loged in!"
	A=False
	B=False
	C=False
	D=False
	form1=UserRegistrationForm(request.POST or None)
	form2=UserProfileForm(request.POST or None)
	if form1.is_valid():
		title='You are registered successfully!'
		user=form1.save(commit=False)
		password=form1.cleaned_data.get('password')
		username=form1.cleaned_data.get('username')
		user.set_password(password)
		user.save()
		new_user=authenticate(username=user.username,password=password)
		login(request,new_user)

		userprofile=form2.save(commit=False)
		userprofile.User=username
		userprofile.user_id=request.user.id
		t=userprofile.save()
		# print(t)
		
		# new_userProfile.save()
	if request.user.is_authenticated():
		logedInUserProfile=UserProfile.objects.get(user_id=request.user.id)
		if logedInUserProfile.A_Value:
			# title+="You are A type user.\n"
			A=True
		if logedInUserProfile.B_Value:
			# title+="You are B type user.\n"
			B=True
		if logedInUserProfile.C_Value:
			C=True
			# title+="You are C type user.\n"
		if logedInUserProfile.D_Value:
			D=True
				# title+="You are D type user.\n"
	return render(request,"userRegister.html",{"form1":form1,"form2":form2,"title":title,"A":A,"B":B,"C":C,"D":D})
	