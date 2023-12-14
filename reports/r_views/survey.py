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
def ReportAllAprovedSurvey(request):
	group = request.user.groups.all()[0].name
	if group == "eip":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		listasurvey = Survey.objects.filter(is_approved=True,village=funsionariu.funsionariu.village).all()
	if group == "fun":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		listasurvey = Survey.objects.filter(is_approved=True,administrativepost=funsionariu.funsionariu.administrativepost).all()
	if group == "admin" or group == "dir":
		listasurvey = Survey.objects.filter(is_approved=True).all()
	context = {
		"title":"Relatoriu Dadus Survey",
		"active_relatoriu":"active",
		"page":"list",
		"listaSurvey":listasurvey,
	}
	return render(request, "survey/SurveyListReport.html",context)