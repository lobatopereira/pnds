from django.db import models
from django.contrib.auth.models import User
from funsionariu.models import Funsionariu
# from programa.models import Implementasaun

# Create your models here.
# Build our Databases and class base objbect.
class ImplementationMonitoring(models.Model):
	FAZE = (
			('Dahuluk I','Dahuluk I'),
			('Daruak II','Daruak II'),
			('Datoluk III','Datoluk III'),
			('Dahaat IV','Dahaat IV'),
			('Dalima V','Dalima V'),
			('Daneen VI','Daneen VI'),
			('Dahitu VII','Dahitu VII'),
			)
	funsionariu = models.ForeignKey(Funsionariu, null=True, on_delete= models.SET_NULL)
	implementasaun = models.ForeignKey('programa.Implementasaun', null=True, on_delete= models.CASCADE,related_name="implementasaun")
	pursentu_programa =models.DecimalField(decimal_places=2,max_digits=10,verbose_name="Pursentu Implementasaun",null=True)
	pursentu_acumulativa =models.DecimalField(decimal_places=2,max_digits=10,verbose_name="Pursentu Acumulativa",null=True)
	orsamentu_gastu = models.DecimalField(decimal_places=2,max_digits=10,verbose_name="Orsamentu Gastus",null=True,blank=True)
	orsamentu_acumulativa = models.DecimalField(decimal_places=2,max_digits=10,verbose_name="Orsamentu Acumulativa",null=True,blank=True)
	ekipamentu_lakompletu = models.CharField(max_length=200, null=True)
	komentariu = models.TextField(null=True, blank=True)
	monitoring_date = models.DateField(auto_now_add=False)
	faze = models.CharField(max_length=200, null=True, choices=FAZE)
	siklu = models.CharField(max_length=200, null=True)
	image = models.ImageField(upload_to='Monitoring', null=True,blank=True)
	is_locked = models.BooleanField(default=False, null=True, blank=True)
	is_sent = models.BooleanField(default=False, null=True, blank=True)
	is_approved = models.BooleanField(default=False, null=True, blank=True)
	is_rejected = models.BooleanField(default=False, null=True, blank=True)
	rejected_info = models.TextField(null=True,blank=True)

	user_created =  models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	hashed = models.CharField(max_length=32, null=True, blank=True)


	def __str__(self):
		template = '{0.implementasaun}'
		return template.format(self)

class PostImplementationMonitoring(models.Model):
	implementasaun = models.ForeignKey('programa.Implementasaun', null=True, on_delete= models.CASCADE,related_name="postImplementasaun")
	funsionariu = models.ForeignKey(Funsionariu, null=True, on_delete= models.SET_NULL)
	monitoring_date = models.DateField(auto_now_add=False)
	kondisaun = models.CharField(choices=[('Diak','Diak'),('Normal','Normal'),('Aat','Aat')],max_length=30,null=True,blank=True)
	komentariu = models.TextField(null=True, blank=True)
	rekomendasaun = models.TextField(null=True, blank=True)
	image = models.ImageField(upload_to='PostMonitoring', null=True,blank=True)
	is_locked = models.BooleanField(default=False, null=True, blank=True)
	is_sent = models.BooleanField(default=False, null=True, blank=True)
	is_approved = models.BooleanField(default=False, null=True, blank=True)
	is_rejected = models.BooleanField(default=False, null=True, blank=True)
	rejected_info = models.TextField(null=True,blank=True)

	user_created =  models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	hashed = models.CharField(max_length=32, null=True, blank=True)


	def __str__(self):
		template = '{0.implementasaun}'
		return template.format(self)	


