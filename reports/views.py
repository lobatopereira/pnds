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
# Create your views here.
@login_required
@allowed_users(allowed_roles=['dir','admin','eip','fun'])
def DashTabularReport(request):
	group = request.user.groups.all()[0].name
	listaPrograma = Programa.objects.all()
	sumariuPrograma = []
	sumariuMunisipiu = []
	statusPrograma = []
	status = Implementasaun.objects.filter(is_approved=True).distinct().values('statusImplementasaun').all()
	statusList = []
	for i in status:
		statusList.append(i['statusImplementasaun'])
	print("status:",statusList)
	if group == "eip":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		listasurvey = Survey.objects.filter(is_approved=True,village=funsionariu.funsionariu.village).all()
		listaimplementasaun = Implementasaun.objects.filter(is_approved=True,village=funsionariu.funsionariu.village).all()
		for x in listaPrograma.iterator():
			totalImplementasaun = Implementasaun.objects.filter(programa__id=x.id,village=funsionariu.funsionariu.village,is_approved=True).count()
			sumariuPrograma.append({'hashed':x.hashed,'naran':x.naran,'totalImplementasaun':totalImplementasaun})
			sumariuProgramaStatus = []
			for cjj in statusList:
				cjj_a = Implementasaun.objects.filter(programa__id=x.id,village=funsionariu.funsionariu.areavillage,is_approved=True,statusImplementasaun=cjj).all().count()
				sumariuProgramaStatus.append({"statusName":cjj,"totalStatus":cjj_a})
			statusPrograma.append({'hashed':x.hashed,'naran':x.naran,'sumariuStatus':sumariuProgramaStatus})
		print("statusPrograma:",statusPrograma)
	if group == "fun":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		listaArea = Village.objects.filter(administrativepost__id=funsionariu.funsionariu.areaadministrativepost.id).all()
		listasurvey = Survey.objects.filter(is_approved=True,administrativepost=funsionariu.funsionariu.administrativepost).all()
		listaimplementasaun = Implementasaun.objects.filter(is_approved=True,administrativepost=funsionariu.funsionariu.administrativepost).all()
		for x in listaPrograma.iterator():
			totalImplementasaun = Implementasaun.objects.filter(programa__id=x.id,administrativepost=funsionariu.funsionariu.areaadministrativepost,is_approved=True).count()
			sumariuPrograma.append({'hashed':x.hashed,'naran':x.naran,'totalImplementasaun':totalImplementasaun})
			sumariuProgramaStatus = []
			for cjj in statusList:
				cjj_a = Implementasaun.objects.filter(programa__id=x.id,administrativepost=funsionariu.funsionariu.areaadministrativepost,is_approved=True,statusImplementasaun=cjj).all().count()
				sumariuProgramaStatus.append({"statusName":cjj,"totalStatus":cjj_a})
			statusPrograma.append({'hashed':x.hashed,'naran':x.naran,'sumariuStatus':sumariuProgramaStatus})
		for x in listaPrograma.iterator():
			totalImplementasaunMun = []
			for cjjM in listaArea.iterator():
				cjjM_a = Implementasaun.objects.filter(programa__id=x.id,village__id=cjjM.id,is_approved=True).all().count()
				totalImplementasaunMun.append({"idSuku":cjjM.id,"suku":cjjM.name,"totalData":cjjM_a})
			sumariuMunisipiu.append({'hashed':x.hashed,'naran':x.naran,'totalImplementasaunMun':totalImplementasaunMun})
		print("sumariuMunisipiu:",sumariuMunisipiu)

		IP_years = Implementasaun.objects.filter().distinct().values('startdate__year').all()
		implementasaun_years = []
		for IPk in IP_years:
			implementasaunyears2 = []
			for IPkk in listaPrograma.iterator():
				IPkk_a = Implementasaun.objects.filter(programa__id=IPkk.id, startdate__year=IPk['startdate__year'], is_approved=True,administrativepost=funsionariu.funsionariu.administrativepost).count()
				implementasaunyears2.append([IPkk.hashed,IPkk_a])
			implementasaun_years.append([IPk['startdate__year'],implementasaunyears2])
	
	if group == "admin" or group == "dir":
		listaArea = Municipality.objects.all()
		listasurvey = Survey.objects.filter(is_approved=True).all()
		listaimplementasaun = Implementasaun.objects.filter(is_approved=True).all()
		for x in listaPrograma.iterator():
			totalImplementasaun = Implementasaun.objects.filter(programa__id=x.id,is_approved=True).count()
			sumariuPrograma.append({'hashed':x.hashed,'naran':x.naran,'totalImplementasaun':totalImplementasaun})
			sumariuProgramaStatus = []
			for cjj in statusList:
				cjj_a = Implementasaun.objects.filter(programa__id=x.id,is_approved=True,statusImplementasaun=cjj).all().count()
				sumariuProgramaStatus.append({"statusName":cjj,"totalStatus":cjj_a})
			statusPrograma.append({'hashed':x.hashed,'naran':x.naran,'sumariuStatus':sumariuProgramaStatus})
		
		for x in listaPrograma.iterator():
			totalImplementasaunMun = []
			for cjjM in listaArea.iterator():
				cjjM_a = Implementasaun.objects.filter(programa__id=x.id,municipality__id=cjjM.id,is_approved=True).all().count()
				totalImplementasaunMun.append({"idMun":cjjM.id,"mun":cjjM.name,"totalData":cjjM_a})
			sumariuMunisipiu.append({'hashed':x.hashed,'naran':x.naran,'totalImplementasaunMun':totalImplementasaunMun})
		print("sumariuMunisipiu:",sumariuMunisipiu)

		IP_years = Implementasaun.objects.filter().distinct().values('startdate__year').all()
		implementasaun_years = []
		for IPk in IP_years:
			implementasaunyears2 = []
			for IPkk in listaPrograma.iterator():
				IPkk_a = Implementasaun.objects.filter(programa__id=IPkk.id, startdate__year=IPk['startdate__year'], is_approved=True).count()
				implementasaunyears2.append([IPkk.hashed,IPkk_a])
			implementasaun_years.append([IPk['startdate__year'],implementasaunyears2])

	context = {
		"title":"Relatoriu Tabular PNDS",
		"active_relatoriu":"active",
		"page":"list",
		"tot_survey":listasurvey.count(),
		"tot_implementasaun":listaimplementasaun.count(),
		"sumariuMunisipiu":sumariuMunisipiu,
		"implementasaun_years":implementasaun_years,
		"sumariuPrograma":sumariuPrograma,
		"listaPrograma":listaPrograma,
		"listaArea":listaArea,
		"statusList":statusList,
		"statusPrograma":statusPrograma,
	}
	return render(request, "tabular/DashTabularReport.html",context)


@login_required
@allowed_users(allowed_roles=['dir','admin','eip','fun'])
def DashGraphReport(request):
	group = request.user.groups.all()[0].name
	if group == "eip":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		listasurvey = Survey.objects.filter(is_approved=True,village=funsionariu.funsionariu.village).all()
		listaimplementasaun = Implementasaun.objects.filter(is_approved=True,village=funsionariu.funsionariu.village).all()
	if group == "fun":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		listasurvey = Survey.objects.filter(is_approved=True,administrativepost=funsionariu.funsionariu.administrativepost).all()
		listaimplementasaun = Implementasaun.objects.filter(is_approved=True,administrativepost=funsionariu.funsionariu.administrativepost).all()
	if group == "admin" or group == "dir":
		listasurvey = Survey.objects.filter(is_approved=True).all()
		listaimplementasaun = Implementasaun.objects.filter(is_approved=True).all()
	context = {
		"title":"Relatoriu Grafiku Programa PNDS",
		"active_relatoriu":"active",
		"page":"list",
		"tot_survey":listasurvey.count(),
		"tot_implementasaun":listaimplementasaun.count(),
	}
	return render(request, "graph/DashGraphReport.html",context)

