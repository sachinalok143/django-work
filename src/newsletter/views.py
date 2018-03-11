from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from .models import signUp,itemDetail
from .forms import signUpForm,ContactForm,itemDetailForm
# Create your views here.

def navbar(request):
	return render(request,"base.html",{}) 
def examplefluid(request):
	return render(request,"example_fluid.html",{}) 

def home(request):
	title="welcome"
	if request.user.is_authenticated():
		title="hi! %s."%(request.user)
	content="%s"%str(request)
	
	form=signUpForm(request.POST or None)
	context={
		"template_title":title,	
		"content":content,
		"form":form,
	}

	if form.is_valid():
		instance = form.save(commit=False)
		# print (instance)
		if not instance.full_name:
			instance.full_name="Sachin"
		instance.save()
		context={
		"template_title":"Thank you!",
		}
	if request.user.is_authenticated() and request.user.is_staff:
		queryset=signUp.objects.all().order_by('-timestamp')
		context={
		"query":queryset
		}

	return render(request,"home.html",context)


def  contact(request):
	form=ContactForm(request.POST or None)
	if form.is_valid():
		# print (form.cleaned_data)
		# for key,value in form.cleaned_data.items():
		# 	print (key,value)

		form_email=form.cleaned_data.get("email")
		form_full_name=form.cleaned_data.get("full_name")
		form_message=form.cleaned_data.get("message")

		subject="Site contact from"
		from_email=settings.EMAIL_HOST_USER
		to_email=[from_email]
		contact_message="%s:%s via %s"%(form_full_name,form_message,form_email)
		send_mail(subject, contact_message, from_email,to_email, fail_silently=False)

		
	context={
		"form":form,
	}
	return render(request,"forms.html",context)

def  addItem(request):
	form=itemDetailForm(request.POST or None)
	context={
		"form":form,
		}
	if form.is_valid():
		instance = form.save(commit=False)
		form_item_name=form.cleaned_data.get("item_name")
		instance.save()
		# form.item_name=''

	if request.user.is_authenticated() and request.user.is_staff:
		queryset=itemDetail.objects.all().order_by('-timestamp')
		context={
		"query":queryset,
		"form": form
		}
		# for x in itemDetail.objects.get(item_name="sachin") :
		# 	print(x)
		# print (itemDetail.objects.filter(item_name="sachin"))

	return render(request,"items.html",context)

# def deleteItem(request,instance):
	# instance.delete()