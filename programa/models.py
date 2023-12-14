from django.db import models
from django.contrib.auth.models import User
from custom.models import *
from survey.models import Survey
from monitoring.models import ImplementationMonitoring,PostImplementationMonitoring

# Create your models here.

class Programa(models.Model):
	naran = models.CharField(max_length=200, null=True)
	user_created =  models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True,blank=True)
	hashed = models.CharField(max_length=32, null=True, blank=True)

	def getTotalImplementation(self):
		return Implementasaun.objects.filter(programa=self,is_approved=True).count()

	def __str__(self):
		template = '{0.naran}'
		return template.format(self)

class Implementasaun(models.Model):
	survey = models.OneToOneField(Survey,on_delete=models.SET_NULL,null=True,blank=True)
	programa = models.ForeignKey(Programa,on_delete=models.CASCADE,null=True)
	village = models.ForeignKey(Village, on_delete=models.CASCADE,null=True)
	administrativepost = models.ForeignKey(AdministrativePost, on_delete=models.CASCADE,null=True)
	municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE,null=True)
	startdate = models.DateField(null=True)
	enddate = models.DateField(null=True)
	montanteOsanAlokasaun = models.DecimalField(default=0,decimal_places=2,max_digits=10,verbose_name="Orsamentu Alokasaun",null=True)
	is_locked = models.BooleanField(default=False, null=True, blank=True)
	is_sent = models.BooleanField(default=False, null=True, blank=True)
	is_approved = models.BooleanField(default=False, null=True, blank=True)
	is_rejected = models.BooleanField(default=False, null=True, blank=True)
	rejected_info = models.TextField(null=True,blank=True)
	description = models.TextField(null=True,blank=True)
	partisipasaunF = models.IntegerField(verbose_name="Partisipasaun Feto",null=True)
	partisipasaunM = models.IntegerField(verbose_name="Partisipasaun Mane",null=True)
	totalTekniku = models.IntegerField(verbose_name="Total Tekniku",null=True)
	partisipasaunP = models.IntegerField(verbose_name="Partisipasaun Populasaun",null=True)
	statusImplementasaun = models.CharField(choices=[('Not Start','Not Start'),('On Going','On Going'),('Pending','Pending'),('Abandone','Abandone'),('Complate','Complate')],default="Not Start",max_length=30,null=True,blank=True)
	image = models.ImageField(upload_to='ImplementasaunPrograma', null=True,blank=True)
	user_created =  models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	hashed = models.CharField(max_length=32, null=True, blank=True)

	def getLastImpelementationMonitoring(self):
		return ImplementationMonitoring.objects.filter(implementasaun=self,is_approved=True).last()

	def getImpelementationMonitoring(self):
		return ImplementationMonitoring.objects.filter(implementasaun=self).all()

	def getPostImpelementationMonitoring(self):
		return PostImplementationMonitoring.objects.filter(implementasaun=self).all()

	def __str__(self):
		template = '{0.programa} {0.village}'
		return template.format(self)

class ImplementasaunPoint(models.Model):
	implementasaun = models.OneToOneField(Implementasaun, on_delete=models.CASCADE, null=True,related_name="implementationLocation")
	latitude = models.CharField(max_length=20, null=True, blank=True)
	longitude = models.CharField(max_length=20, null=True, blank=True)
	image = models.ImageField(upload_to='implementationLocation', null=True,blank=True)

	def __str__(self):
		template = '{0.implementasaun}'
		return template.format(self)