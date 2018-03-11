from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User
class UserProfile(models.Model):
	user=models.OneToOneField(User)
	A_Value = models.BooleanField(default=False)
	B_Value = models.BooleanField(default=False)
	C_Value = models.BooleanField(default=False)
	D_Value = models.BooleanField(default=False)
	Address=models.CharField(max_length=500,blank=True,null=True)
	Phone=models.DecimalField(max_digits=10, decimal_places=False)
	# E_Value = models.BooleanField(default=False)
