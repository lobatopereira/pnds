from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from django.contrib.auth.models import Group,User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..models import *
from programa.models import Implementasaun
from custom.utils import *
from custom.models import *
from ..forms import *
from funsionariu.models import UserFunsionariu
from users.decorators import allowed_users

@login_required
@allowed_users(allowed_roles=['eip','fun'])
def addMonitoringImplementasaun(request,hashid):
	implementasaun = get_object_or_404(Implementasaun,hashed=hashid)
	group = request.user.groups.all()[0].name
	funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
	funsionariuId = get_object_or_404(Funsionariu,id=funsionariu.funsionariu.id)
	
	if request.method == "POST":
		_, newid = getlastid(ImplementationMonitoring)
		hashid = hash_md5(str(newid))
		form = MonitoringForm(request.POST,request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.hashed = hashid
			instance.implementasaun = implementasaun
			instance.funsionariu = funsionariuId
			instance.user_created = request.user
			pursentu_programa = instance.pursentu_programa
			orsamentu_gastu = instance.orsamentu_gastu
			monitoringData = ImplementationMonitoring.objects.filter(implementasaun=implementasaun).last()
			if monitoringData:
				instance.orsamentu_acumulativa = float(orsamentu_gastu) + float(monitoringData.orsamentu_acumulativa)
				instance.pursentu_acumulativa = float(pursentu_programa) + float(monitoringData.pursentu_acumulativa)
			else:
				instance.orsamentu_acumulativa = float(orsamentu_gastu) + float(0)
				instance.pursentu_acumulativa = float(pursentu_programa) + float(0)
			instance.save()
			messages.success(request, f'Dadus Monitoring Prosesu Implementasaun Programa Adisiona ho Susesu.')
			return redirect('detalluImplementasaunPrograma',implementasaun.hashed)
	else:
		form = MonitoringForm()
	context ={
		"title":f"Formulariu Monitoring Implementasaun Programa {implementasaun.programa} iha Suku {implementasaun.village}",
		"form":form,
		"implementasaun":implementasaun,
		"page":"form",
	}
	return render(request,'monitoring/FormMonitoringImplementasaun.html',context)

@login_required
@allowed_users(allowed_roles=['fun','eip'])
def updateMonitoringImplementasaun(request,hashid,page):
	monitoring = get_object_or_404(ImplementationMonitoring,hashed=hashid)
	implementasaun = get_object_or_404(Implementasaun,hashed=monitoring.implementasaun.hashed)
	group = request.user.groups.all()[0].name
	funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
	if request.method == "POST":
		form = MonitoringForm(request.POST,request.FILES,instance=monitoring)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			messages.success(request, f'Dadus Monitoring Prosesu Implementasaun Programa Altera ho Susesu.')
			if page == "list":
				return redirect('detalluImplementasaunPrograma',monitoring.implementasaun.hashed)
			if page == "notifList":
				return redirect('NotifMonitoringImplementationReject')
	else:
		form = MonitoringForm(instance=monitoring)
	context ={
		"title":f"Formulariu Monitoring Implementasaun Programa {monitoring.implementasaun.programa} iha Suku {monitoring.implementasaun.village}",
		"form":form,
		"implementasaun":implementasaun,
		"page":"form",
	}
	return render(request,'monitoring/FormMonitoringImplementasaun.html',context)


@login_required
@allowed_users(allowed_roles=['fun','eip'])
def lockMonitoringImplementasaunPrograma(request,hashid,page):
	implementasaunData = get_object_or_404(ImplementationMonitoring,hashed=hashid)
	implementasaunData.is_locked = True
	implementasaunData.save()
	messages.success(request, f'Dadus MonitoringImplementasaun Programa {implementasaunData.implementasaun.programa} iha suku {implementasaunData.implementasaun.village} Xave ho Susesu.')
	if page == "list":
		return redirect('detalluImplementasaunPrograma',implementasaunData.implementasaun.hashed)
	if page == "notifList":
		return redirect('NotifMonitoringImplementationReject')

@login_required
@allowed_users(allowed_roles=['eip','fun'])
def unlockMonitoringImplementasaunPrograma(request,hashid,page):
	implementasaunData = get_object_or_404(ImplementationMonitoring,hashed=hashid)
	implementasaunData.is_locked = False
	implementasaunData.save()
	messages.success(request, f'Dadus Monitoring Implementasaun Programa {implementasaunData.implementasaun.programa} iha suku {implementasaunData.implementasaun.village} Loke ho Susesu.')
	if page == "list":
		return redirect('detalluImplementasaunPrograma',implementasaunData.implementasaun.hashed)
	if page == "notifList":
		return redirect('NotifMonitoringImplementationReject')

@login_required
@allowed_users(allowed_roles=['eip','fun'])
def mandaMonitoringImplementasaunPrograma(request,hashid,page):
	implementasaunData = get_object_or_404(ImplementationMonitoring,hashed=hashid)
	implementasaunData.is_sent = True
	implementasaunData.is_rejected = False
	implementasaunData.save()
	messages.warning(request, f'Dadus Monitoring Implementasaun Programa {implementasaunData.implementasaun.programa} iha suku {implementasaunData.implementasaun.village} Manda ho Susesu.')
	if page == "list":
		return redirect('detalluImplementasaunPrograma',implementasaunData.implementasaun.hashed)
	if page == "notifList":
		return redirect('NotifMonitoringImplementationReject')
