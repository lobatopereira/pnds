from django.db import models
from django.contrib.auth.models import User
from custom.models import *

class Survey(models.Model):
	programa = models.ForeignKey('programa.Programa',on_delete=models.CASCADE,null=True)
	village = models.ForeignKey(Village, on_delete=models.CASCADE,null=True,verbose_name="Survey iha Suku ne'ebe?")
	administrativepost = models.ForeignKey(AdministrativePost, on_delete=models.CASCADE,null=True,verbose_name="Survey iha Postu ne'ebe?")
	municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE,null=True,verbose_name="Survey iha Munisipiu ne'ebe?")
	aldeia = models.CharField(max_length=222, null=True, blank=True,verbose_name="Survey iha Aldeia ka bairu ne'ebe?")
	surveyDate = models.DateField(null=True,verbose_name="Data Survey")
	totalUmakain = models.IntegerField(verbose_name="Total Umakain",null=True)
	image = models.ImageField(upload_to='SurveyImage', null=True,blank=True,verbose_name="Upload Imajen Survey")
	description = models.TextField(null=True,blank=True,verbose_name="Informasaun Adisional")
	
	is_locked = models.BooleanField(default=False, null=True, blank=True)
	is_sent = models.BooleanField(default=False, null=True, blank=True)
	is_approved = models.BooleanField(default=False, null=True, blank=True)
	is_rejected = models.BooleanField(default=False, null=True, blank=True)
	is_implemented = models.BooleanField(default=False, null=True, blank=True)
	rejected_info = models.TextField(null=True,blank=True)

	user_created =  models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	hashed = models.CharField(max_length=32, null=True, blank=True)

	def __str__(self):
		template = '{0.programa}, Aldeia : {0.aldeia}, Data : {0.surveyDate}'
		return template.format(self)