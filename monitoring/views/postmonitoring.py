from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from django.contrib.auth.models import Group,User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..models import *
from custom.utils import *
from custom.models import *
from ..forms import *
from funsionariu.models import UserFunsionariu
from programa.models import Implementasaun
from users.decorators import allowed_users

@login_required
@allowed_users(allowed_roles=['fun','eip'])
def addPostMonitoringImplementasaun(request,hashid):
	implementasaun = get_object_or_404(Implementasaun,hashed=hashid)
	group = request.user.groups.all()[0].name
	funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
	funsionariuId = get_object_or_404(Funsionariu,id=funsionariu.funsionariu.id)
	if request.method == "POST":
		_, newid = getlastid(PostImplementationMonitoring)
		hashid = hash_md5(str(newid))
		form = PostImplementationMonitoringForm(request.POST,request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.hashed = hashid
			instance.implementasaun = implementasaun
			instance.funsionariu = funsionariuId
			instance.user_created = request.user
			instance.save()
			messages.success(request, f'Dadus Monitoring Post Implementasaun Programa Adisiona ho Susesu.')
			return redirect('detalluImplementasaunPrograma',implementasaun.hashed)
	else:
		form = PostImplementationMonitoringForm()
	context ={
		"title":f"Formulariu Monitoring Post Implementasaun Programa {implementasaun.programa} iha Suku {implementasaun.village}",
		"form":form,
		"implementasaun":implementasaun,
		"page":"form",
	}
	return render(request,'monitoring/FormMonitoringImplementasaun.html',context)

@login_required
@allowed_users(allowed_roles=['fun','eip'])
def updateMonitoringPostImplementasaun(request,hashid,page):
	implementasaun = get_object_or_404(PostImplementationMonitoring,hashed=hashid)
	if request.method == "POST":
		form = PostImplementationMonitoringForm(request.POST,request.FILES,instance=implementasaun)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			messages.success(request, f'Dadus Monitoring Post Implementasaun Programa Altera ho Susesu.')
			if page == "list":
				return redirect('detalluImplementasaunPrograma',implementasaun.implementasaun.hashed)
			if page == "notifList":
				return redirect('NotifMonitoringPostImplementationReject')
	else:
		form = PostImplementationMonitoringForm(instance=implementasaun)
	context ={
		"title":f"Formulariu Altera Monitoring Post Implementasaun Programa {implementasaun.implementasaun.programa} iha Suku {implementasaun.implementasaun.village}",
		"form":form,
		"implementasaun":implementasaun,
		"page":"form",
	}
	return render(request,'monitoring/FormMonitoringImplementasaun.html',context)

@login_required
@allowed_users(allowed_roles=['fun','eip'])
def lockMonitoringPostImplementasaunPrograma(request,hashid,page):
	implementasaunData = get_object_or_404(PostImplementationMonitoring,hashed=hashid)
	implementasaunData.is_locked = True
	implementasaunData.save()
	messages.success(request, f'Dadus Monitoring Post Implementasaun Programa {implementasaunData.implementasaun.programa} iha suku {implementasaunData.implementasaun.village} Xave ho Susesu.')
	if page == "list":
		return redirect('detalluImplementasaunPrograma',implementasaunData.implementasaun.hashed)
	if page == "notifList":
		return redirect('NotifMonitoringPostImplementationReject')

@login_required
@allowed_users(allowed_roles=['eip','fun'])
def unlockMonitoringPostImplementasaunPrograma(request,hashid,page):
	implementasaunData = get_object_or_404(PostImplementationMonitoring,hashed=hashid)
	implementasaunData.is_locked = False
	implementasaunData.save()
	messages.success(request, f'Dadus Monitoring Post Implementasaun Programa {implementasaunData.implementasaun.programa} iha suku {implementasaunData.implementasaun.village} Loke ho Susesu.')
	if page == "list":
		return redirect('detalluImplementasaunPrograma',implementasaunData.implementasaun.hashed)
	if page == "notifList":
		return redirect('NotifMonitoringPostImplementationReject')

@login_required
@allowed_users(allowed_roles=['eip','fun'])
def mandaMonitoringPostImplementasaunPrograma(request,hashid,page):
	implementasaunData = get_object_or_404(PostImplementationMonitoring,hashed=hashid)
	implementasaunData.is_sent = True
	implementasaunData.is_rejected = False
	implementasaunData.save()
	messages.warning(request, f'Dadus Monitoring Post Implementasaun Programa {implementasaunData.implementasaun.programa} iha suku {implementasaunData.implementasaun.village} Manda ho Susesu.')
	if page == "list":
		return redirect('detalluImplementasaunPrograma',implementasaunData.implementasaun.hashed)
	if page == "notifList":
		return redirect('NotifMonitoringPostImplementationReject')
