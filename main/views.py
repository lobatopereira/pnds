from django.shortcuts import render, redirect
from django.http import HttpResponse
from monitoring.models import *
from programa.models import Programa,Implementasaun,ImplementationMonitoring
from funsionariu.models import Funsionariu
from django.contrib.auth.models import User,Group
from custom.utils import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from users.decorators import allowed_users
# Create your views here.

@login_required
def home(request):
	programa = Programa.objects.all()
	monitoring = ImplementationMonitoring.objects.all()
	funsionariu = Funsionariu.objects.all()
	implementasaun = Implementasaun.objects.all()
	ongoingImplementasaun = Implementasaun.objects.filter(statusImplementasaun="On Going").all()
	context= {
		'programa':programa, 
		'monitoring':monitoring, 
		'funsionariu':funsionariu,
		'implementasaun':implementasaun,
		'ongoingImplementasaun':ongoingImplementasaun,
	}

	return render (request, 'index/indexAdmin.html',context)