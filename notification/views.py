from django.shortcuts import render, get_object_or_404,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from users.decorators import allowed_users
from programa.models import Implementasaun
from monitoring.models import ImplementationMonitoring,PostImplementationMonitoring
from django.contrib import messages
from funsionariu.models import UserFunsionariu
from survey.models import Survey
# Create your views here.

@login_required
@allowed_users(allowed_roles=['dir'])
def NotifImplementationSent(request):
	group = request.user.groups.all()[0].name
	objects = Implementasaun.objects.filter(is_sent=True, is_approved=False).all().order_by('-startdate')
	context = {
		'group': group, 'objects': objects, 'page': 'notifList',
		'title': 'Lista Implementasaun', 'legend': 'Lista Implementasaun'
	}
	return render(request, 'notification/listaImplementasaun.html', context)

@login_required
@allowed_users(allowed_roles=['dir'])
def NotifSurveySent(request):
	group = request.user.groups.all()[0].name
	objects = Survey.objects.filter(is_sent=True, is_approved=False).all().order_by('-surveyDate')
	context = {
		'group': group, 'objects': objects, 'page': 'list',
		'title': 'Lista Survey', 'legend': 'Lista Survey'
	}
	return render(request, 'notification/listaSurvey.html', context)

@login_required
@allowed_users(allowed_roles=['eip'])
def NotifImplementationReject(request):
	group = request.user.groups.all()[0].name
	funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
	objects = Implementasaun.objects.filter(village=funsionariu.funsionariu.village, is_sent=False, is_approved=False, is_rejected=True).all().order_by('-startdate')
	context = {
		'group': group, 'objects': objects, 'page': 'notifList',
		'title': 'Lista Implementasaun', 'legend': 'Lista Implementasaun'
	}
	return render(request, 'notification/listaImplementasaunRejected.html', context)


@login_required
@allowed_users(allowed_roles=['dir'])
def approvedImplementasaunPrograma(request,hashid,page):
	implementasaunData = get_object_or_404(Implementasaun,hashed=hashid)
	implementasaunData.is_approved = True
	implementasaunData.save()
	messages.success(request, f'Dadus Implementasaun Programa {implementasaunData.programa} iha suku {implementasaunData.village} Aprova / Valida ona ho Susesu.')
	if page == "list":
		return redirect('ListaImplementasaun')
	else:
		return redirect('detalluImplementasaunProgramaNotif',implementasaunData.hashed)

@login_required
@allowed_users(allowed_roles=['dir'])
def approvedMonitoringPostImplementasaunPrograma(request,hashid):
	postImplementationData = get_object_or_404(PostImplementationMonitoring,hashed=hashid)
	postImplementationData.is_approved = True
	postImplementationData.save()
	messages.success(request, f'Dadus Monitorizasaun Post Implementasaun {postImplementationData.implementasaun.programa} iha suku {postImplementationData.implementasaun.village} Aprova / Valida ona ho Susesu.')
	return redirect('NotifMonitoringImplementationSent')

@login_required
@allowed_users(allowed_roles=['dir'])
def approvedMonitoringImplementasaunPrograma(request,hashid):
	implementasaunData = get_object_or_404(ImplementationMonitoring,hashed=hashid)
	implementasaunData.is_approved = True
	implementasaunData.save()
	messages.success(request, f'Dadus Monitorizasaun Implementasaun Programa {implementasaunData.implementasaun.programa} iha suku {implementasaunData.implementasaun.village} Aprova / Valida ona ho Susesu.')
	return redirect('detalluImplementasaunPrograma',implementasaunData.implementasaun.hashed)


@login_required
@allowed_users(allowed_roles=['dir'])
def NotifMonitoringImplementationSent(request):
	group = request.user.groups.all()[0].name
	objects = ImplementationMonitoring.objects.filter(is_sent=True, is_approved=False).all().order_by('-monitoring_date')
	context = {
		'group': group, 'objects': objects, 'page': 'notifList',
		'title': 'Lista Monitorizasaun Implementasaun', 'legend': 'Lista Monitorizasaun Implementasaun'
	}
	return render(request, 'notification/listaMonitoringImplementasaun.html', context)

@login_required
@allowed_users(allowed_roles=['dir'])
def NotifMonitoringPostImplementationSent(request):
	group = request.user.groups.all()[0].name
	objects = PostImplementationMonitoring.objects.filter(is_sent=True, is_approved=False).all().order_by('-monitoring_date')
	context = {
		'group': group, 'objects': objects, 'page': 'notifList',
		'title': 'Lista Monitorizasaun Post Implementasaun', 'legend': 'Lista Monitorizasaun Post Implementasaun'
	}
	return render(request, 'notification/listaMonitoringPostImplementasaun.html', context)

@login_required
@allowed_users(allowed_roles=['dir'])
def rejeitaImplementasaunPrograma(request):
	hashid = request.GET['hashed']
	page = request.GET['list']
	rejeita_info = request.GET['rejeita_info']
	implementasaunData = get_object_or_404(Implementasaun,hashed=hashid)
	implementasaunData.is_rejected = True
	implementasaunData.is_sent = False
	implementasaunData.rejected_info = rejeita_info
	implementasaunData.save()
	messages.success(request, f'Dadus Implementasaun Programa {implementasaunData.programa} iha suku {implementasaunData.village} Rejeita ho Susesu.')
	if page == "list":
		return redirect('ListaImplementasaun')
	else:
		return redirect('detalluImplementasaunProgramaNotif',implementasaunData.hashed)


@login_required
@allowed_users(allowed_roles=['dir'])
def detalluImplementasaunProgramaNotif(request,hashid):
	group = request.user.groups.all()[0].name
	implementasaunData = get_object_or_404(Implementasaun,hashed=hashid)
	context = {
		'group': group, 'objects': implementasaunData, 'page': 'detail',
		'title': 'Detallu Dadus Implementasaun', 'legend': 'Detallu Dadus Implementasaun'
	}
	return render(request, 'notification/listaImplementasaun.html', context)

@login_required
@allowed_users(allowed_roles=['dir'])
def detalluSurveyNotif(request,hashid):
	group = request.user.groups.all()[0].name
	surveyData = get_object_or_404(Survey,hashed=hashid)
	context = {
		'group': group, 'objects': surveyData, 'page': 'detail',
		'title': 'Detallu Dadus Survey', 'legend': 'Detallu Dadus Survey'
	}
	return render(request, 'notification/listaSurvey.html', context)


@login_required
@allowed_users(allowed_roles=['dir'])
def approvedSurvey(request,hashid,page):
	surveyData = get_object_or_404(Survey,hashed=hashid)
	surveyData.is_approved = True
	surveyData.save()
	messages.success(request, f'Dadus Survey {surveyData.programa} iha suku {surveyData.village} Aprova / Valida ona ho Susesu.')
	if page == "list":
		return redirect('ListaSurvey')
	else:
		return redirect('detalluSurveyNotif',surveyData.hashed)

@login_required
@allowed_users(allowed_roles=['dir'])
def rejeitaSurvey(request):
	hashid = request.GET['hashed']
	page = request.GET['list']
	rejeita_info = request.GET['rejeita_info']
	surveyData = get_object_or_404(Survey,hashed=hashid)
	surveyData.is_rejected = True
	surveyData.is_sent = False
	surveyData.rejected_info = rejeita_info
	surveyData.save()
	messages.success(request, f'Dadus Survey {surveyData.programa} iha suku {surveyData.village} Rejeita ho Susesu.')
	if page == "list":
		return redirect('ListaSurvey')
	else:
		return redirect('detalluSurveyNotif',surveyData.hashed)

@login_required
@allowed_users(allowed_roles=['fun'])
def NotifSurveyReject(request):
	group = request.user.groups.all()[0].name
	funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
	objects = Survey.objects.filter(administrativepost=funsionariu.funsionariu.areaadministrativepost,is_sent=False, is_approved=False, is_rejected=True).all().order_by('-surveyDate')
	context = {
		'group': group, 'objects': objects, 'page': 'notifList',
		'title': 'Lista Survey Rejeitadu', 'legend': 'Lista Survey Rejeitadu'
	}
	return render(request, 'notification/listaSurveyRejected.html', context)

@login_required
@allowed_users(allowed_roles=['dir'])
def rejeitaMonitoringImplementasaunPrograma(request):
	hashid = request.GET['hashed']
	page = request.GET['list']
	rejeita_info = request.GET['rejeita_info']
	implementasaunData = get_object_or_404(ImplementationMonitoring,hashed=hashid)
	implementasaunData.is_rejected = True
	implementasaunData.is_sent = False
	implementasaunData.rejected_info = rejeita_info
	implementasaunData.save()
	messages.success(request, f'Dadus Monitoring Implementasaun Programa {implementasaunData.implementasaun.programa} iha suku {implementasaunData.implementasaun.village} Rejeita ho Susesu.')
	if page == "list":
		return redirect('NotifMonitoringImplementationSent')

@login_required
@allowed_users(allowed_roles=['dir'])
def rejeitaMonitoringPostImplementasaunPrograma(request):
	hashid = request.GET['hashed']
	page = request.GET['list']
	rejeita_info = request.GET['rejeita_info']
	implementasaunData = get_object_or_404(PostImplementationMonitoring,hashed=hashid)
	implementasaunData.is_rejected = True
	implementasaunData.is_sent = False
	implementasaunData.rejected_info = rejeita_info
	implementasaunData.save()
	messages.success(request, f'Dadus Monitoring Post Implementasaun Programa {implementasaunData.implementasaun.programa} iha suku {implementasaunData.implementasaun.village} Rejeita ho Susesu.')
	if page == "list":
		return redirect('NotifMonitoringPostImplementationSent')

@login_required
@allowed_users(allowed_roles=['fun'])
def NotifMonitoringImplementationReject(request):
	group = request.user.groups.all()[0].name
	funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
	objects = ImplementationMonitoring.objects.filter(implementasaun__administrativepost=funsionariu.funsionariu.areaadministrativepost,is_sent=False, is_approved=False, is_rejected=True).all().order_by('-monitoring_date')
	context = {
		'group': group, 'objects': objects, 'page': 'notifList',
		'title': 'Lista Dadus Monitoring Implementasaun Rejeitadu', 'legend': 'Lista Dadus Monitoring Implementasaun Rejeitadu'
	}
	return render(request, 'notification/listaMonitoringImplementationRejected.html', context)

@login_required
@allowed_users(allowed_roles=['fun'])
def NotifMonitoringPostImplementationReject(request):
	group = request.user.groups.all()[0].name
	funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
	objects = PostImplementationMonitoring.objects.filter(implementasaun__administrativepost=funsionariu.funsionariu.areaadministrativepost,is_sent=False, is_approved=False, is_rejected=True).all().order_by('-monitoring_date')
	context = {
		'group': group, 'objects': objects, 'page': 'notifList',
		'title': 'Lista Dadus Monitoring Post Implementasaun Rejeitadu', 'legend': 'Lista Dadus Monitoring Post Implementasaun Rejeitadu'
	}
	return render(request, 'notification/listaMonitoringPostImplementationRejected.html', context)
