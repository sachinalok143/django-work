from django.db import models

# Create your models here.

class signUp(models.Model):
	email=models.EmailField()
	full_name=models.CharField(max_length=120,blank=True,null=True)
	timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
	updated=models.DateTimeField(auto_now_add=False,auto_now=True)

	def __str__ (self): #	python 3.3 is __str__
		return self.email

class itemDetail(models.Model):
	# email=models.EmailField()
	item_name=models.CharField(max_length=120,blank=False,null=False)
	timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
	updated=models.DateTimeField(auto_now_add=False,auto_now=True)

	def __str__ (self): #	python 3.3 is __str__
		return self.item_name

