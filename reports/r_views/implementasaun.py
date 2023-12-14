from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from django.contrib.auth.models import Group,User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from programa.models import *
from custom.utils import *
from custom.models import *
from survey.models import *
from funsionariu.models import UserFunsionariu
from users.decorators import allowed_users

@login_required
@allowed_users(allowed_roles=['dir','admin','eip','fun'])
def ReportAllAprovedImplementation(request):
	group = request.user.groups.all()[0].name
	if group == "eip":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		listaImplementasaun = Implementasaun.objects.filter(is_approved=True,village=funsionariu.funsionariu.village).all()
	if group == "fun":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		listaImplementasaun = Implementasaun.objects.filter(is_approved=True,administrativepost=funsionariu.funsionariu.administrativepost).all()
	if group == "admin" or group == "dir":
		listaImplementasaun = Implementasaun.objects.filter(is_approved=True).all()
	context = {
		"title":"Relatoriu Dadus Survey",
		"active_relatoriu":"active",
		"page":"list",
		"listaImplementasaun":listaImplementasaun,
	}
	return render(request, "implementasaun/ImplementationListReport.html",context)

@login_required
@allowed_users(allowed_roles=['dir','admin','eip','fun'])
def ReportImplementasaunPrograma(request,hashid):
	programaData = get_object_or_404(Programa,hashed=hashid)
	group = request.user.groups.all()[0].name
	if group == "eip":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		listaImplementasaun = Implementasaun.objects.filter(programa=programaData,is_approved=True,village=funsionariu.funsionariu.village).all()
	if group == "fun":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		listaImplementasaun = Implementasaun.objects.filter(programa=programaData,is_approved=True,administrativepost=funsionariu.funsionariu.administrativepost).all()
	if group == "admin" or group == "dir":
		listaImplementasaun = Implementasaun.objects.filter(programa=programaData,is_approved=True).all()
	context = {
		"title":f"Relatoriu Dadus Implementasaun Programa {programaData.naran}",
		"active_relatoriu":"active",
		"page":"list",
		"listaImplementasaun":listaImplementasaun,
	}
	return render(request, "implementasaun/ImplementationListReport.html",context)

@login_required
@allowed_users(allowed_roles=['dir','admin','eip','fun'])
def ReportStatusImplementasaunPrograma(request,hashidProgram,status):
	programaData = get_object_or_404(Programa,hashed=hashidProgram)
	group = request.user.groups.all()[0].name
	if group == "eip":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		listaImplementasaun = Implementasaun.objects.filter(programa=programaData,statusImplementasaun=status,is_approved=True,village=funsionariu.funsionariu.village).all()
	if group == "fun":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		listaImplementasaun = Implementasaun.objects.filter(programa=programaData,statusImplementasaun=status,is_approved=True,administrativepost=funsionariu.funsionariu.administrativepost).all()
	if group == "admin" or group == "dir":
		listaImplementasaun = Implementasaun.objects.filter(programa=programaData,statusImplementasaun=status,is_approved=True).all()
	context = {
		"title":f"Relatoriu Dadus Implementasaun Programa {programaData.naran} ho Estadu {status}",
		"active_relatoriu":"active",
		"page":"list",
		"listaImplementasaun":listaImplementasaun,
	}
	return render(request, "implementasaun/ImplementationListReport.html",context)

@login_required
@allowed_users(allowed_roles=['dir','admin','eip','fun'])
def ReportTinanImplementasaunPrograma(request,tinan,hashidProgram):
	programaData = get_object_or_404(Programa,hashed=hashidProgram)
	group = request.user.groups.all()[0].name
	if group == "eip":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		listaImplementasaun = Implementasaun.objects.filter(programa=programaData,startdate__year=tinan,is_approved=True,village=funsionariu.funsionariu.village).all()
	if group == "fun":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		listaImplementasaun = Implementasaun.objects.filter(programa=programaData,startdate__year=tinan,is_approved=True,administrativepost=funsionariu.funsionariu.administrativepost).all()
	if group == "admin" or group == "dir":
		listaImplementasaun = Implementasaun.objects.filter(programa=programaData,startdate__year=tinan,is_approved=True).all()
	context = {
		"title":f"Relatoriu Dadus Implementasaun Programa {programaData.naran} iha Tinan {tinan}",
		"active_relatoriu":"active",
		"page":"list",
		"listaImplementasaun":listaImplementasaun,
	}
	return render(request, "implementasaun/ImplementationListReport.html",context)

@login_required
@allowed_users(allowed_roles=['dir','admin','eip','fun'])
def ReportSukuImplementasaunPrograma(request,hashidProgram,suku):
	programaData = get_object_or_404(Programa,hashed=hashidProgram)
	villageData = get_object_or_404(Village,id=suku)
	group = request.user.groups.all()[0].name
	funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
	listaImplementasaun = Implementasaun.objects.filter(programa=programaData,village=villageData,is_approved=True).all()
	context = {
		"title":f"Relatoriu Dadus Implementasaun Programa {programaData.naran} iha Suku {villageData.name}",
		"active_relatoriu":"active",
		"page":"list",
		"listaImplementasaun":listaImplementasaun,
	}
	return render(request, "implementasaun/ImplementationListReport.html",context)

@login_required
@allowed_users(allowed_roles=['dir','admin','eip','fun'])
def ReportMunisipiuImplementasaunPrograma(request,hashidProgram,munisipiu):
	programaData = get_object_or_404(Programa,hashed=hashidProgram)
	municipalityData = get_object_or_404(Municipality,id=munisipiu)
	group = request.user.groups.all()[0].name
	listaImplementasaun = Implementasaun.objects.filter(programa=programaData,municipality=municipalityData,is_approved=True).all()
	context = {
		"title":f"Relatoriu Dadus Implementasaun Programa {programaData.naran} iha Munisipiu {municipalityData.name}",
		"active_relatoriu":"active",
		"page":"list",
		"listaImplementasaun":listaImplementasaun,
	}
	return render(request, "implementasaun/ImplementationListReport.html",context)
