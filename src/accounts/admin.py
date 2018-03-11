from django.contrib import admin
from .models import UserProfile 
from .forms import UserProfileForm
# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
	list_display=["user","A_Value","B_Value","C_Value","D_Value","Address","Phone"]
	form=UserProfileForm
	class Meta:
		model = UserProfile

admin.site.register(UserProfile,UserProfileAdmin)