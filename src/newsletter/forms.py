from django import forms
from .models import signUp,itemDetail

class ContactForm(forms.Form):
	full_name=forms.CharField(required=False)
	email=forms.EmailField()
	message=forms.CharField()
	

class signUpForm(forms.ModelForm):
	class Meta:
		model=signUp
		fields=['email',"full_name"]
	
	def clean_email(self):
		# print (self.cleaned_data)
		email=self.cleaned_data.get("email")
		email_base,provider=email.split("@")
		domain,extention=provider.split(".")
		if not extention == "com":
			raise forms.ValidationError("Please use a valid .com email address!")
		return email

	def clean_fulll_name(self):
		full_name=self.cleaned_data.get("full_name")
		#put validation code here
		return full_name

class itemDetailForm(forms.ModelForm):
	class Meta:
		model=itemDetail
		fields=["item_name"]
	def clean_fulll_name(self):
		item_name=self.cleaned_data.get("item_name")
		#put validation code here
		return item_name