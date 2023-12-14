from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from django.contrib.auth.models import Group,User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..models import *
from custom.utils import *
from ..forms import *
from funsionariu.models import UserFunsionariu
from users.decorators import allowed_users
# Create your views here.
@login_required
@allowed_users(allowed_roles=['dir','admin','eip','fun'])
def ListaPrograma(request):
	group = request.user.groups.all()[0].name
	listaPrograma = Programa.objects.all()
	sumariuPrograma = []
	if group == "eip":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		for x in listaPrograma.iterator():
			totalImplementasaun = Implementasaun.objects.filter(programa__id=x.id,village=funsionariu.funsionariu.village).count()
			sumariuPrograma.append({'hashed':x.hashed,'naran':x.naran,'totalImplementasaun':totalImplementasaun})
	if group == "fun":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		for x in listaPrograma.iterator():
			totalImplementasaun = Implementasaun.objects.filter(programa__id=x.id,administrativepost=funsionariu.funsionariu.areaadministrativepost).count()
			sumariuPrograma.append({'hashed':x.hashed,'naran':x.naran,'totalImplementasaun':totalImplementasaun})
	if group == "admin" or group == "dir":
		for x in listaPrograma.iterator():
			totalImplementasaun = Implementasaun.objects.filter(programa__id=x.id,is_approved=True).count()
			sumariuPrograma.append({'hashed':x.hashed,'naran':x.naran,'totalImplementasaun':totalImplementasaun})
	context = {
		"title":"Sumariu Programa PNDS",
		"active_programa":"active",
		"page":"list",
		"listaPrograma":sumariuPrograma,
	}
	return render(request, "ListaPrograma.html",context)

@login_required
@allowed_users(allowed_roles=['dir','admin'])
def addPrograma(request):
	if request.method == "POST":
		_, newid = getlastid(Programa)
		hashid = hash_md5(str(newid))
		form = ProgramaForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.hashed = hashid
			instance.user_created = request.user
			instance.save()
			messages.success(request, f'Dadus Programa Adisiona ho Susesu.')
			return redirect('ListaPrograma')
	else:
		form = ProgramaForm()
	
	context ={
		"title":"Adisiona Programa",
		"form":form,
		"active_programa":"active",
		"page":"form",
	}
	return render(request,'ListaPrograma.html',context)
	
@login_required
@allowed_users(allowed_roles=['dir','admin','eip','fun'])
def listaImplementasaunPrograma(request,hashid):
	group = request.user.groups.all()[0].name
	programa = get_object_or_404(Programa,hashed=hashid)
	if group == "eip":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		listaImplementasaun = Implementasaun.objects.filter(programa=programa,village=funsionariu.funsionariu.village).all().order_by('-id')
		listaPrograma = Programa.objects.all()
		sumariuPrograma = []
		for x in listaPrograma.iterator():
			totalImplementasaun = Implementasaun.objects.filter(programa__id=x.id,village=funsionariu.funsionariu.village).count()
			sumariuPrograma.append({'hashed':x.hashed,'naran':x.naran,'totalImplementasaun':totalImplementasaun})
	if group == "fun":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		listaImplementasaun = Implementasaun.objects.filter(programa=programa,administrativepost=funsionariu.funsionariu.areaadministrativepost).all().order_by('-id')
		listaPrograma = Programa.objects.all()
		sumariuPrograma = []
		for x in listaPrograma.iterator():
			totalImplementasaun = Implementasaun.objects.filter(programa__id=x.id,administrativepost=funsionariu.funsionariu.areaadministrativepost).count()
			sumariuPrograma.append({'hashed':x.hashed,'naran':x.naran,'totalImplementasaun':totalImplementasaun})
	if group == "admin" or group == "dir":
		listaImplementasaun = Implementasaun.objects.filter(programa=programa,is_approved=True).all().order_by('-id')
		listaPrograma = Programa.objects.all()
		sumariuPrograma = []
		for x in listaPrograma.iterator():
			totalImplementasaun = Implementasaun.objects.filter(programa__id=x.id,is_approved=True).count()
			sumariuPrograma.append({'hashed':x.hashed,'naran':x.naran,'totalImplementasaun':totalImplementasaun})
	context = {
		"title":f"Lista Implementasaun Programa {programa.naran}",
		"listaImplementasaun":listaImplementasaun,
		"sumariuPrograma":sumariuPrograma,
	}
	return render(request, "ListaImplementasaunPrograma.html",context)