from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from programa.models import Programa
from funsionariu.models import Funsionariu
from django.contrib.auth.models import User,Group
from custom.utils import *
from django.contrib import messages
from funsionariu.models import Funsionariu,UserFunsionariu
from custom.models import Municipality,AdministrativePost,Village
from django.contrib.auth.decorators import login_required
from users.decorators import allowed_users
from .models import Survey
from .forms import SurveyForm1,SurveyForm2
# Create your views here.

@login_required
@allowed_users(allowed_roles=['eip','fun','admin','dir'])
def ListaSurvey(request):
	group = request.user.groups.all()[0].name
	if group == "fun":
		listaSurvey = Survey.objects.all()
	elif group == "admin" or group == "dir":
		listaSurvey = Survey.objects.filter(is_approved=True).all()
	context = {
		"title":"Lista Survey PNDS",
		"active_survey":"active",
		"page":"list",
		"listaSurvey":listaSurvey,
	}
	return render(request, "survey/ListaSurvey.html",context)

@login_required
@allowed_users(allowed_roles=['eip','fun'])
def AddSurvey(request):
	group = request.user.groups.all()[0].name
	if group == "eip":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		village = get_object_or_404(Village,id=funsionariu.funsionariu.areavillage.id)
		administrativepost = get_object_or_404(AdministrativePost,id=village.administrativepost.id)
		municipality = get_object_or_404(Municipality,id=administrativepost.municipality.id)
		if request.method == "POST":
			_, newid = getlastid(Survey)
			hashid = hash_md5(str(newid))
			form = SurveyForm2(request.POST,request.FILES)
			if form.is_valid():
				instance = form.save(commit=False)
				instance.hashed = hashid
				instance.village = village
				instance.village = village
				instance.administrativepost = administrativepost
				instance.municipality = municipality
				instance.user_created = request.user
				instance.save()
				messages.success(request, f'Dadus Survey Programa Adisiona ho Susesu.')
				return redirect('ListaSurvey')
		else:
			form = SurveyForm2()
	if group == "fun":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		administrativepost = get_object_or_404(AdministrativePost,id=funsionariu.funsionariu.areaadministrativepost.id)
		municipality = get_object_or_404(Municipality,id=administrativepost.municipality.id)
		if request.method == "POST":
			_, newid = getlastid(Survey)
			hashid = hash_md5(str(newid))
			form = SurveyForm1(request.POST,request.FILES,administrativepost=administrativepost)
			if form.is_valid():
				instance = form.save(commit=False)
				instance.hashed = hashid
				instance.administrativepost = administrativepost
				instance.municipality = municipality
				instance.user_created = request.user
				instance.save()
				messages.success(request, f'Dadus Survey Programa Adisiona ho Susesu.')
				return redirect('ListaSurvey')
		else:
			form = SurveyForm1(administrativepost=administrativepost)
	context ={
		"title":"Formulariu Rejistu Survey PNDS",
		"form":form,
		"active_survey":"active",
		"page":"form",
	}
	return render(request, "survey/ListaSurvey.html",context)

@login_required
@allowed_users(allowed_roles=['eip','fun'])
def UpdateSurvey(request,hashid,page):
	surveyData = get_object_or_404(Survey,hashed=hashid)
	group = request.user.groups.all()[0].name
	if group == "eip":
		if request.method == "POST":
			form = SurveyForm2(request.POST,request.FILES,instance=surveyData)
			if form.is_valid():
				instance = form.save(commit=False)
				instance.save()
				messages.success(request, f'Dadus Survey Programa Altera ho Susesu.')
				if page == "list":
					return redirect('ListaSurvey')
				elif page == "detail":
					return redirect('detalluSurveyData',surveyData.hashed)
		else:
			form = SurveyForm2(instance=surveyData)
	if group == "fun":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		administrativepost = get_object_or_404(AdministrativePost,id=funsionariu.funsionariu.areaadministrativepost.id)
		if request.method == "POST":
			form = SurveyForm1(request.POST,request.FILES,instance=surveyData,administrativepost=administrativepost)
			if form.is_valid():
				instance = form.save(commit=False)
				instance.save()
				messages.success(request, f'Dadus Survey Programa Altera ho Susesu.')
				if page == "list":
					return redirect('ListaSurvey')
				elif page == "detail":
					return redirect('detalluSurveyData',surveyData.hashed)
				elif page == "notifList":
					return redirect('NotifSurveyReject')
		else:
			form = SurveyForm1(instance=surveyData,administrativepost=administrativepost)
	context ={
		"title":"Formulariu Altera Dadus Survey PNDS",
		"form":form,
		"active_survey":"active",
		"page":"form",
	}
	return render(request, "survey/ListaSurvey.html",context)

@login_required
@allowed_users(allowed_roles=['eip','fun'])
def lockSurveyData(request,hashid,page):
	surveyData = get_object_or_404(Survey,hashed=hashid)
	surveyData.is_locked = True
	surveyData.save()
	messages.success(request, f'Dadus Survey {surveyData.programa} iha suku {surveyData.village} Xave ho Susesu.')
	if page == "list":
		return redirect('ListaSurvey')
	elif page == "notifList":
		return redirect('NotifSurveyReject')
	elif page == "detail":
		return redirect('detalluSurveyData',surveyData.hashed)

@login_required
@allowed_users(allowed_roles=['eip','fun'])
def unlockSurveyData(request,hashid,page):
	surveyData = get_object_or_404(Survey,hashed=hashid)
	surveyData.is_locked = False
	surveyData.save()
	messages.success(request, f'Dadus Survey {surveyData.programa} iha suku {surveyData.village} Loke ho Susesu.')
	if page == "list":
		return redirect('ListaSurvey')
	elif page == "notifList":
		return redirect('NotifSurveyReject')
	elif page == "detail":
		return redirect('detalluSurveyData',surveyData.hashed)

@login_required
@allowed_users(allowed_roles=['eip','fun'])
def mandaSurveyData(request,hashid,page):
	surveyData = get_object_or_404(Survey,hashed=hashid)
	surveyData.is_sent = True
	surveyData.is_rejected = False
	surveyData.save()
	messages.error(request, f'Dadus Survey {surveyData.programa} iha suku {surveyData.village} Manda ho Susesu.')
	if page == "list":
		return redirect('ListaSurvey')
	elif page == "notifList":
		return redirect('NotifSurveyReject')
	else:
		return redirect('detalluSurveyData',surveyData.hashed)

@login_required
@allowed_users(allowed_roles=['eip','fun','admin','dir'])
def detalluSurveyData(request,hashid):
	surveyData = get_object_or_404(Survey,hashed=hashid)
	context ={
		"title":f"Detallu Dadus Survey {surveyData.programa} iha Suku {surveyData.village}",
		"surveyData":surveyData,
		"active_survey":"active",
	}
	return render(request, "survey/DetalluSurvey.html",context)
	