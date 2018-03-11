from django.contrib import admin

from .forms import signUpForm
from .models import signUp,itemDetail
# from SomeOtherAppp import SomeOtherModel


# Register your models here.

class signUpAdmin(admin.ModelAdmin):
	list_display=["__str__","full_name","timestamp","updated"]
	form=signUpForm
	class Meta:
		model = signUp
		

class itemDetailAdmin(admin.ModelAdmin):
	list_display=["__str__","timestamp","updated"]
	form=signUpForm
	class meta:
		model=itemDetail
		
admin.site.register(signUp,signUpAdmin)

admin.site.register(itemDetail,itemDetailAdmin)
