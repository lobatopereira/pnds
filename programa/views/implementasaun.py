from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from django.contrib.auth.models import Group,User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..models import *
from custom.utils import *
from custom.models import *
from ..forms import *
from funsionariu.models import UserFunsionariu
from users.decorators import allowed_users
# Create your views here.
@login_required
@allowed_users(allowed_roles=['dir','admin','eip','fun'])
def ListaImplementasaun(request):
	group = request.user.groups.all()[0].name
	if group == "eip":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		listaInplementasaun = Implementasaun.objects.filter(village=funsionariu.funsionariu.areavillage).all().order_by('-id')
		listaPrograma = Programa.objects.all()
		sumariuPrograma = []
		for x in listaPrograma.iterator():
			totalImplementasaun = Implementasaun.objects.filter(programa__id=x.id,village=funsionariu.funsionariu.areavillage).count()
			sumariuPrograma.append({'hashed':x.hashed,'naran':x.naran,'totalImplementasaun':totalImplementasaun})
	if group == "fun":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		listaInplementasaun = Implementasaun.objects.filter(administrativepost=funsionariu.funsionariu.areaadministrativepost).all().order_by('-id')
		listaPrograma = Programa.objects.all()
		sumariuPrograma = []
		for x in listaPrograma.iterator():
			totalImplementasaun = Implementasaun.objects.filter(programa__id=x.id,administrativepost=funsionariu.funsionariu.areaadministrativepost).count()
			sumariuPrograma.append({'hashed':x.hashed,'naran':x.naran,'totalImplementasaun':totalImplementasaun})
	if group == "admin" or group == "dir":
		listaInplementasaun = Implementasaun.objects.filter(is_approved=True).all().order_by('-id')
		listaPrograma = Programa.objects.all()
		sumariuPrograma = []
		for x in listaPrograma.iterator():
			totalImplementasaun = Implementasaun.objects.filter(programa__id=x.id,is_approved=True).count()
			sumariuPrograma.append({'hashed':x.hashed,'naran':x.naran,'totalImplementasaun':totalImplementasaun})
	context = {
		"title":"Lista Implementasaun Programa PNDS",
		"active_programa":"active",
		"page":"list",
		"sumariuPrograma":sumariuPrograma,
		"listaInplementasaun":listaInplementasaun,
	}
	return render(request, "ListaImplementasaun.html",context)

@login_required
@allowed_users(allowed_roles=['admin','eip','fun','dir'])
def addImplementasaun(request):
	group = request.user.groups.all()[0].name
	if group == "eip":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		village = get_object_or_404(Village,id=funsionariu.funsionariu.areavillage.id)
		administrativepost = get_object_or_404(AdministrativePost,id=village.administrativepost.id)
		municipality = get_object_or_404(Municipality,id=administrativepost.municipality.id)
		if request.method == "POST":
			_, newid = getlastid(Implementasaun)
			hashid = hash_md5(str(newid))
			form = ImplementasaunForm1(request.POST,request.FILES)
			if form.is_valid():
				instance = form.save(commit=False)
				instance.hashed = hashid
				instance.village = village
				instance.administrativepost = administrativepost
				instance.municipality = municipality
				instance.user_created = request.user
				instance.save()
				messages.success(request, f'Dadus Implementasaun Programa Adisiona ho Susesu.')
				return redirect('addImplementationLocation', hashid)
		else:
			form = ImplementasaunForm1()
	if group == "fun":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		administrativepost = get_object_or_404(AdministrativePost,id=funsionariu.funsionariu.areaadministrativepost.id)
		municipality = get_object_or_404(Municipality,id=administrativepost.municipality.id)
		if request.method == "POST":
			_, newid = getlastid(Implementasaun)
			hashid = hash_md5(str(newid))
			form = ImplementasaunForm2(request.POST,request.FILES,administrativepost=administrativepost)
			if form.is_valid():
				instance = form.save(commit=False)
				instance.hashed = hashid
				instance.administrativepost = administrativepost
				instance.municipality = municipality
				instance.user_created = request.user
				instance.save()
				messages.success(request, f'Dadus Implementasaun Programa Adisiona ho Susesu.')
				return redirect('addImplementationLocation', hashid)
		else:
			form = ImplementasaunForm2(administrativepost=administrativepost)
	if group == "admin" or group == "dir":
		if request.method == "POST":
			_, newid = getlastid(Implementasaun)
			hashid = hash_md5(str(newid))
			form = ImplementasaunForm(request.POST,request.FILES)
			if form.is_valid():
				instance = form.save(commit=False)
				instance.hashed = hashid
				instance.user_created = request.user
				instance.save()
				messages.success(request, f'Dadus Implementasaun Programa Adisiona ho Susesu.')
				return redirect('addImplementationLocation', hashid)
		else:
			form = ImplementasaunForm()
	
	context ={
		"title":"Formulariu Rejistu Implementasaun",
		"form":form,
		"active_programa":"active",
		"page":"form",
	}
	return render(request,'ListaImplementasaun.html',context)

@login_required
@allowed_users(allowed_roles=['admin','eip','fun'])
def updateImplementasaun(request,hashid,page):
	implementasaun = get_object_or_404(Implementasaun,hashed=hashid)
	if request.method == "POST":
		form = ImplementasaunForm(request.POST,request.FILES,instance=implementasaun)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			messages.success(request, f'Dadus Implementasaun Programa Altera ho Susesu.')
			if page == "list":
				return redirect('ListaImplementasaun')
			if page == "notiflist":
				return redirect('NotifImplementationReject')
			if page == "detail":
				return redirect('detalluImplementasaunPrograma',implementasaun.hashed)
	else:
		form = ImplementasaunForm(instance=implementasaun)
	
	context ={
		"title":"Formulariu Altera Implementasaun",
		"form":form,
		"active_programa":"active",
		"page":"form",
	}
	return render(request,'ListaImplementasaun.html',context)

@login_required
@allowed_users(allowed_roles=['dir','eip','admin','fun'])
def detalluImplementasaunPrograma(request,hashid):
	implementasaun = get_object_or_404(Implementasaun,hashed=hashid)
	lastMonitoringData = ImplementationMonitoring.objects.filter(implementasaun=implementasaun,is_approved=True).last()
	# print("lastMonitoringData:",lastMonitoringData)
	context ={
		"title":f"Detallu Implementasaun Programa {implementasaun.programa}",
		"implementasaun":implementasaun,
		"lastMonitoringData":lastMonitoringData,
		"active_programa":"active",
	}
	return render(request,'DetalluImplementasaun.html',context)
	
@login_required
@allowed_users(allowed_roles=['admin','eip','fun'])
def deleteImplementasaun(request,hashid):
	implementasaunData = get_object_or_404(Implementasaun,hashed=hashid)
	implementasaunData.delete()
	messages.error(request, f'Dadus Implementasaun Programa {implementasaunData.programa} iha suku {implementasaunData.village} Delete ho Susesu.')
	return redirect('ListaImplementasaun')

@login_required
@allowed_users(allowed_roles=['admin','eip','fun'])
def updateStatusImplementasaun(request):
	implementasaunHashed = request.GET['hashed']
	status = request.GET['status']
	implementasaunData = get_object_or_404(Implementasaun,hashed=implementasaunHashed)
	implementasaunData.statusImplementasaun = status 
	implementasaunData.save()
	messages.success(request, f'Dadus Status Implementasaun Programa {implementasaunData.programa} iha suku {implementasaunData.village} Update ho Susesu.')
	return redirect('detalluImplementasaunPrograma',implementasaunData.hashed)


@login_required
@allowed_users(allowed_roles=['admin','eip','fun'])
def lockImplementasaunPrograma(request,hashid,page):
	implementasaunData = get_object_or_404(Implementasaun,hashed=hashid)
	implementasaunData.is_locked = True
	implementasaunData.save()
	messages.success(request, f'Dadus Implementasaun Programa {implementasaunData.programa} iha suku {implementasaunData.village} Xave ho Susesu.')
	if page == "list":
		return redirect('ListaImplementasaun')
	if page == "notif":
		return redirect('NotifImplementationReject')
	else:
		return redirect('detalluImplementasaunPrograma',implementasaunData.hashed)

@login_required
@allowed_users(allowed_roles=['eip','admin','fun'])
def unlockImplementasaunPrograma(request,hashid,page):
	implementasaunData = get_object_or_404(Implementasaun,hashed=hashid)
	implementasaunData.is_locked = False
	implementasaunData.save()
	messages.success(request, f'Dadus Implementasaun Programa {implementasaunData.programa} iha suku {implementasaunData.village} Loke ho Susesu.')
	if page == "list":
		return redirect('ListaImplementasaun')
	if page == "notif":
		return redirect('NotifImplementationReject')
	else:
		return redirect('detalluImplementasaunPrograma',implementasaunData.hashed)

@login_required
@allowed_users(allowed_roles=['eip','admin','fun'])
def mandaImplementasaunPrograma(request,hashid,page):
	implementasaunData = get_object_or_404(Implementasaun,hashed=hashid)
	implementasaunData.is_sent = True
	implementasaunData.is_rejected = False
	implementasaunData.save()
	messages.warning(request, f'Dadus Implementasaun Programa {implementasaunData.programa} iha suku {implementasaunData.village} Manda ho Susesu.')
	if page == "list":
		return redirect('ListaImplementasaun')
	else:
		return redirect('detalluImplementasaunPrograma',implementasaunData.hashed)


@login_required
@allowed_users(allowed_roles=['eip','admin','fun'])
def addImplementationLocation(request,hashid):
	implementasaunData = get_object_or_404(Implementasaun, hashed=hashid)
	if request.method == "POST":
		latitude = request.POST.get('lat')
		longitude = request.POST.get('lng')
		ImplementasaunPoint.objects.create(implementasaun=implementasaunData,latitude=latitude,longitude=longitude)
		messages.success(request, f'Lokalizasaun Implementasaun Programa {implementasaunData.programa} iha Suku {implementasaunData.village} Adisiona ho Susesu.')
		return redirect('ListaImplementasaun')
	context ={
		"title":f"Adisiona Lokalizasaun Implementasaun Programa {implementasaunData.programa}",
		"active_programa":"active",
		"page":"addLocation",
	}
	return render(request,'ListaImplementasaun.html',context)

@login_required
@allowed_users(allowed_roles=['eip','admin','fun'])
def updateMapaLokalizasaunImplementasaun(request,hashid):
	implementasaunLocationData = get_object_or_404(ImplementasaunPoint, id=hashid)
	if request.method == "POST":
		latitude = request.POST.get('lat')
		longitude = request.POST.get('lng')
		ImplementasaunPoint.objects.filter(id=hashid).update(latitude=latitude,longitude=longitude)
		messages.success(request, f'Lokalizasaun Implementasaun Programa {implementasaunLocationData.implementasaun.programa} iha Suku {implementasaunLocationData.implementasaun.village} Update ho Susesu.')
		return redirect('detalluImplementasaunPrograma',implementasaunLocationData.implementasaun.hashed)
	context ={
		"title":f"Update Lokalizasaun Implementasaun Programa {implementasaunLocationData.implementasaun.programa} iha Suku {implementasaunLocationData.implementasaun.village}",
		"active_programa":"active",
		"page":"addLocation",
	}
	return render(request,'ListaImplementasaun.html',context)

@login_required
@allowed_users(allowed_roles=['dir','admin','eip','fun'])
def mapaLokalizasaunImplementasaunPrograma(request):
	group = request.user.groups.all()[0].name
	if group == "eip":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		mapaImplementasaun = ImplementasaunPoint.objects.filter(implementasaun__village=funsionariu.funsionariu.areavillage).all()
	if group == "fun":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		mapaImplementasaun = ImplementasaunPoint.objects.filter(implementasaun__administrativepost__id=funsionariu.funsionariu.areaadministrativepost.id).all()
	if group == "admin" or group == "dir":
		mapaImplementasaun = ImplementasaunPoint.objects.filter(implementasaun__is_approved=True).all()
	context ={
		"title":f"Mapa Lokalizasaun Implementasaun Programa PNDS",
		"active_programa":"active",
		"mapaImplementasaun":mapaImplementasaun,
	}
	return render(request,'MapaListaImplementasaun.html',context)
