from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import Group,User
from django.contrib.auth.decorators import login_required
from programa.models import *
from custom.utils import *
from funsionariu.models import UserFunsionariu

@login_required
def ChartSumariuPrograma(request):
	group = request.user.groups.all()[0].name
	labels = []
	data = []
	listaPrograma = Programa.objects.all()
	if group == "eip":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		for x in listaPrograma.iterator():
			totalImplementasaun = Implementasaun.objects.filter(programa__id=x.id,village=funsionariu.funsionariu.village).count()
			labels.append(x.naran)
			data.append(totalImplementasaun)
	if group == "fun":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		for x in listaPrograma.iterator():
			totalImplementasaun = Implementasaun.objects.filter(programa__id=x.id,administrativepost=funsionariu.funsionariu.administrativepost).count()
			labels.append(x.naran)
			data.append(totalImplementasaun)
	if group == "admin" or group == "dir":
		for x in listaPrograma.iterator():
			totalImplementasaun = Implementasaun.objects.filter(programa__id=x.id,is_approved=True).count()
			labels.append(x.naran)
			data.append(totalImplementasaun)

	return JsonResponse(data={
		'labels':labels,
		'data':data,
		})

@login_required
def ChartStatusImplementasaunPrograma(request):
	group = request.user.groups.all()[0].name
	listaPrograma = Programa.objects.all()
	status = Implementasaun.objects.filter(is_approved=True).distinct().values('statusImplementasaun').all()
	label,obj,programLabel,statusList = list(),list(),list(),list()
	for a in listaPrograma.iterator():
		programLabel.append(a.naran)
	for i in status:
		statusList.append(i['statusImplementasaun'])
	if group == "eip":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		for cjj in statusList:
			totalImplementasaun = []
			for x in listaPrograma.iterator():
				cjj_a = Implementasaun.objects.filter(programa__id=x.id,village=funsionariu.funsionariu.areavillage,is_approved=True,statusImplementasaun=cjj).all().count()
				totalImplementasaun.append(cjj_a)
			label.append(cjj)
			obj.append(totalImplementasaun)
	if group == "fun":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		for cjj in statusList:
			totalImplementasaun = []
			for x in listaPrograma.iterator():
				cjj_a = Implementasaun.objects.filter(programa__id=x.id,administrativepost=funsionariu.funsionariu.areaadministrativepost,is_approved=True,statusImplementasaun=cjj).all().count()
				totalImplementasaun.append(cjj_a)
			label.append(cjj)
			obj.append(totalImplementasaun)
	if group == "admin" or group == "dir":
		for cjj in statusList:
			totalImplementasaun = []
			for x in listaPrograma.iterator():
				cjj_a = Implementasaun.objects.filter(programa__id=x.id,is_approved=True,statusImplementasaun=cjj).all().count()
				totalImplementasaun.append(cjj_a)
			label.append(cjj)
			obj.append(totalImplementasaun)

	return JsonResponse(data={
		'programLabels':programLabel,
		'labels':label,
		'data':obj,
		})

@login_required
def ChartImplementasaunProgramaArea(request):
	group = request.user.groups.all()[0].name
	listaPrograma = Programa.objects.all()
	label,obj,programLabel = list(),list(),list()
	for a in listaPrograma.iterator():
		programLabel.append(a.naran)
	if group == "eip":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		for cjj in statusList:
			totalImplementasaun = []
			for x in listaPrograma.iterator():
				cjj_a = Implementasaun.objects.filter(programa__id=x.id,village=funsionariu.funsionariu.areavillage,is_approved=True,statusImplementasaun=cjj).all().count()
				totalImplementasaun.append(cjj_a)
			label.append(cjj)
			obj.append(totalImplementasaun)
	if group == "fun":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		listaArea = Village.objects.filter(administrativepost__id=funsionariu.funsionariu.areaadministrativepost.id).all()
		for cjj in listaArea.iterator():
			totalImplementasaun = []
			for x in listaPrograma.iterator():
				cjj_a = Implementasaun.objects.filter(programa__id=x.id,village__id=cjj.id,is_approved=True).all().count()
				totalImplementasaun.append(cjj_a)
			label.append(cjj.name)
			obj.append(totalImplementasaun)
	if group == "admin" or group == "dir":
		listaArea = Municipality.objects.all()
		for cjj in listaArea.iterator():
			totalImplementasaun = []
			for x in listaPrograma.iterator():
				cjj_a = Implementasaun.objects.filter(programa__id=x.id,municipality__id=cjj.id,is_approved=True).all().count()
				totalImplementasaun.append(cjj_a)
			label.append(cjj.name)
			obj.append(totalImplementasaun)
	return JsonResponse(data={
		'programLabels':programLabel,
		'labels':label,
		'data':obj,
		})


@login_required
def ChartImplementasaunProgramaYear(request):
	group = request.user.groups.all()[0].name
	listaPrograma = Programa.objects.all()
	label,obj,programLabel = list(),list(),list()
	for a in listaPrograma.iterator():
		programLabel.append(a.naran)
	if group == "eip":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		for cjj in statusList:
			totalImplementasaun = []
			for x in listaPrograma.iterator():
				cjj_a = Implementasaun.objects.filter(programa__id=x.id,village=funsionariu.funsionariu.areavillage,is_approved=True,statusImplementasaun=cjj).all().count()
				totalImplementasaun.append(cjj_a)
			label.append(cjj)
			obj.append(totalImplementasaun)
	if group == "fun":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		IP_years = Implementasaun.objects.filter(administrativepost__id=funsionariu.funsionariu.areaadministrativepost.id).distinct().values('startdate__year').all()
		for cjj in IP_years.iterator():
			totalImplementasaun = []
			for x in listaPrograma.iterator():
				cjj_a = Implementasaun.objects.filter(administrativepost__id=funsionariu.funsionariu.areaadministrativepost.id,programa__id=x.id, startdate__year=cjj['startdate__year'], is_approved=True).count()
				totalImplementasaun.append(cjj_a)
			label.append(cjj['startdate__year'])
			obj.append(totalImplementasaun)
	if group == "admin" or group == "dir":
		IP_years = Implementasaun.objects.filter().distinct().values('startdate__year').all()
		for cjj in IP_years.iterator():
			totalImplementasaun = []
			for x in listaPrograma.iterator():
				cjj_a = Implementasaun.objects.filter(programa__id=x.id, startdate__year=cjj['startdate__year'], is_approved=True).count()
				totalImplementasaun.append(cjj_a)
			label.append(cjj['startdate__year'])
			obj.append(totalImplementasaun)

	return JsonResponse(data={
		'programLabels':programLabel,
		'labels':label,
		'data':obj,
		})


