from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from django.contrib.auth.models import Group,User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from programa.models import ImplementasaunPoint,Programa,Implementasaun
from custom.utils import *
from custom.models import *
from funsionariu.models import UserFunsionariu
from users.decorators import allowed_users

# Create your views here.
@login_required
@allowed_users(allowed_roles=['dir','admin','eip','fun'])
def DashMaps(request):
	group = request.user.groups.all()[0].name
	topSideObjects = Programa.objects.all()
	rightSideObjects = list()
	if group == "eip":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		mapaImplementasaun = ImplementasaunPoint.objects.filter(implementasaun__village=funsionariu.funsionariu.areavillage).all()
		rightData = Municipality.objects.all()
		for x in rightData.iterator():
			totalMapaImplementasaun = ImplementasaunPoint.objects.filter(implementasaun__municipality__id=x.id).all().count()
			rightSideObjects.append({"hashed":x.id,"name":x.name,"totData":totalMapaImplementasaun})
	if group == "fun":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		mapaImplementasaun1 = ImplementasaunPoint.objects.filter(implementasaun__statusImplementasaun="Not Start",implementasaun__administrativepost__id=funsionariu.funsionariu.areaadministrativepost.id).all()
		mapaImplementasaun2 = ImplementasaunPoint.objects.filter(implementasaun__statusImplementasaun="On Going",implementasaun__administrativepost__id=funsionariu.funsionariu.areaadministrativepost.id).all()
		mapaImplementasaun3 = ImplementasaunPoint.objects.filter(implementasaun__statusImplementasaun="Pending",implementasaun__administrativepost__id=funsionariu.funsionariu.areaadministrativepost.id).all()
		mapaImplementasaun4 = ImplementasaunPoint.objects.filter(implementasaun__statusImplementasaun="Abandone",implementasaun__administrativepost__id=funsionariu.funsionariu.areaadministrativepost.id).all()
		mapaImplementasaun5 = ImplementasaunPoint.objects.filter(implementasaun__statusImplementasaun="Complate",implementasaun__administrativepost__id=funsionariu.funsionariu.areaadministrativepost.id).all()
		rightData = Village.objects.filter(administrativepost__id=funsionariu.funsionariu.areaadministrativepost.id).all()
		for x in rightData.iterator():
			totalMapaImplementasaun = ImplementasaunPoint.objects.filter(implementasaun__village__id=x.id).all().count()
			rightSideObjects.append({"hashed":x.id,"name":x.name,"totData":totalMapaImplementasaun})
	if group == "admin" or group == "dir":
		mapaImplementasaun1 = ImplementasaunPoint.objects.filter(implementasaun__statusImplementasaun="Not Start",implementasaun__is_approved=True).all()
		mapaImplementasaun2 = ImplementasaunPoint.objects.filter(implementasaun__statusImplementasaun="On Going",implementasaun__is_approved=True).all()
		mapaImplementasaun3 = ImplementasaunPoint.objects.filter(implementasaun__statusImplementasaun="Pending",implementasaun__is_approved=True).all()
		mapaImplementasaun4 = ImplementasaunPoint.objects.filter(implementasaun__statusImplementasaun="Abandone",implementasaun__is_approved=True).all()
		mapaImplementasaun5 = ImplementasaunPoint.objects.filter(implementasaun__statusImplementasaun="Complate",implementasaun__is_approved=True).all()
		rightData = Municipality.objects.all()
		rightData = Municipality.objects.all()
		for x in rightData.iterator():
			totalMapaImplementasaun = ImplementasaunPoint.objects.filter(implementasaun__municipality__id=x.id).all().count()
			rightSideObjects.append({"hashed":x.id,"name":x.name,"totData":totalMapaImplementasaun})
	context = {
		"title":f"Mapa Lokalizasaun Implementasaun Programa PNDS",
		"active_maps":"active",
		"mapaImplementasaun1":mapaImplementasaun1,
		"mapaImplementasaun2":mapaImplementasaun2,
		"mapaImplementasaun3":mapaImplementasaun3,
		"mapaImplementasaun4":mapaImplementasaun4,
		"mapaImplementasaun5":mapaImplementasaun5,
		"topSideObjects":topSideObjects,
		"rightSideObjects":rightSideObjects,
	}
	return render(request,'dashMaps.html',context)

@login_required
@allowed_users(allowed_roles=['dir','admin','eip','fun'])
def MapaImplementasaunMunisipiu(request, hashid):
	group = request.user.groups.all()[0].name
	municipalityData = get_object_or_404(Municipality,id=hashid)
	programaLista = Programa.objects.all()
	topSideObjects = list()
	for x in programaLista.iterator():
		implementasaunMun = Implementasaun.objects.filter(programa__id=x.id,municipality__id=municipalityData.id,is_approved=True).count()
		topSideObjects.append({"hashed":x.hashed,"name":x.naran,"totData":implementasaunMun})
	rightSideObjects = list()
	if group == "eip":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		mapaImplementasaun = ImplementasaunPoint.objects.filter(implementasaun__village=funsionariu.funsionariu.areavillage).all()
		rightData = Municipality.objects.all()
		for x in rightData.iterator():
			totalMapaImplementasaun = ImplementasaunPoint.objects.filter(implementasaun__municipality__id=x.id).all().count()
			rightSideObjects.append({"hashed":x.id,"name":x.name,"totData":totalMapaImplementasaun})
	if group == "fun":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		mapaImplementasaun1 = ImplementasaunPoint.objects.filter(implementasaun__statusImplementasaun="Not Start",implementasaun__administrativepost__id=funsionariu.funsionariu.areaadministrativepost.id).all()
		mapaImplementasaun2 = ImplementasaunPoint.objects.filter(implementasaun__statusImplementasaun="On Going",implementasaun__administrativepost__id=funsionariu.funsionariu.areaadministrativepost.id).all()
		mapaImplementasaun3 = ImplementasaunPoint.objects.filter(implementasaun__statusImplementasaun="Pending",implementasaun__administrativepost__id=funsionariu.funsionariu.areaadministrativepost.id).all()
		mapaImplementasaun4 = ImplementasaunPoint.objects.filter(implementasaun__statusImplementasaun="Abandone",implementasaun__administrativepost__id=funsionariu.funsionariu.areaadministrativepost.id).all()
		mapaImplementasaun5 = ImplementasaunPoint.objects.filter(implementasaun__statusImplementasaun="Complate",implementasaun__administrativepost__id=funsionariu.funsionariu.areaadministrativepost.id).all()
		rightData = Village.objects.filter(administrativepost__id=funsionariu.funsionariu.areaadministrativepost.id).all()
		for x in rightData.iterator():
			totalMapaImplementasaun = ImplementasaunPoint.objects.filter(implementasaun__village__id=x.id).all().count()
			rightSideObjects.append({"hashed":x.id,"name":x.name,"totData":totalMapaImplementasaun})
	if group == "admin" or group == "dir":
		mapaImplementasaun1 = ImplementasaunPoint.objects.filter(implementasaun__statusImplementasaun="Not Start",implementasaun__is_approved=True,implementasaun__municipality__id=municipalityData.id).all()
		mapaImplementasaun2 = ImplementasaunPoint.objects.filter(implementasaun__statusImplementasaun="On Going",implementasaun__is_approved=True,implementasaun__municipality__id=municipalityData.id).all()
		mapaImplementasaun3 = ImplementasaunPoint.objects.filter(implementasaun__statusImplementasaun="Pending",implementasaun__is_approved=True,implementasaun__municipality__id=municipalityData.id).all()
		mapaImplementasaun4 = ImplementasaunPoint.objects.filter(implementasaun__statusImplementasaun="Abandone",implementasaun__is_approved=True,implementasaun__municipality__id=municipalityData.id).all()
		mapaImplementasaun5 = ImplementasaunPoint.objects.filter(implementasaun__statusImplementasaun="Complate",implementasaun__is_approved=True,implementasaun__municipality__id=municipalityData.id).all()
		rightData = AdministrativePost.objects.filter(municipality__id=municipalityData.id).all()
		for x in rightData.iterator():
			totalMapaImplementasaun = ImplementasaunPoint.objects.filter(implementasaun__administrativepost__id=x.id).all().count()
			rightSideObjects.append({"hashed":x.id,"name":x.name,"totData":totalMapaImplementasaun})
	context = {
		"title":f"Mapa Lokalizasaun Implementasaun Programa PNDS - Munisipiu {municipalityData.name}",
		"active_maps":"active",
		"mapaImplementasaun1":mapaImplementasaun1,
		"mapaImplementasaun2":mapaImplementasaun2,
		"mapaImplementasaun3":mapaImplementasaun3,
		"mapaImplementasaun4":mapaImplementasaun4,
		"mapaImplementasaun5":mapaImplementasaun5,
		"topSideObjects":topSideObjects,
		"rightSideObjects":rightSideObjects,
	}
	return render(request,'MapsImplementationMunisipiu.html',context)

@login_required
@allowed_users(allowed_roles=['dir','admin','eip','fun'])
def MapaImplementasaunPostu(request, hashid):
	group = request.user.groups.all()[0].name
	postuData = get_object_or_404(AdministrativePost,id=hashid)
	programaLista = Programa.objects.all()
	topSideObjects = list()
	for x in programaLista.iterator():
		implementasaunMun = Implementasaun.objects.filter(programa__id=x.id,administrativepost__id=postuData.id,is_approved=True).count()
		topSideObjects.append({"hashed":x.hashed,"name":x.naran,"totData":implementasaunMun})
	rightSideObjects = list()
	if group == "eip":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		mapaImplementasaun = ImplementasaunPoint.objects.filter(implementasaun__village=funsionariu.funsionariu.areavillage).all()
		rightData = Village.objects.get(administrativepost__id=postuData.id)
		for x in rightData.iterator():
			totalMapaImplementasaun = ImplementasaunPoint.objects.filter(administrativepost__village__id=x.id).all().count()
			rightSideObjects.append({"hashed":x.id,"name":x.name,"totData":totalMapaImplementasaun})
	if group == "fun":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		mapaImplementasaun1 = ImplementasaunPoint.objects.filter(implementasaun__statusImplementasaun="Not Start",implementasaun__administrativepost__id=funsionariu.funsionariu.areaadministrativepost.id).all()
		mapaImplementasaun2 = ImplementasaunPoint.objects.filter(implementasaun__statusImplementasaun="On Going",implementasaun__administrativepost__id=funsionariu.funsionariu.areaadministrativepost.id).all()
		mapaImplementasaun3 = ImplementasaunPoint.objects.filter(implementasaun__statusImplementasaun="Pending",implementasaun__administrativepost__id=funsionariu.funsionariu.areaadministrativepost.id).all()
		mapaImplementasaun4 = ImplementasaunPoint.objects.filter(implementasaun__statusImplementasaun="Abandone",implementasaun__administrativepost__id=funsionariu.funsionariu.areaadministrativepost.id).all()
		mapaImplementasaun5 = ImplementasaunPoint.objects.filter(implementasaun__statusImplementasaun="Complate",implementasaun__administrativepost__id=funsionariu.funsionariu.areaadministrativepost.id).all()
		rightData = Village.objects.filter(administrativepost__id=postuData.id).all()
		for x in rightData.iterator():
			totalMapaImplementasaun = ImplementasaunPoint.objects.filter(implementasaun__village__id=x.id).all().count()
			rightSideObjects.append({"hashed":x.id,"name":x.name,"totData":totalMapaImplementasaun})
	if group == "admin" or group == "dir":
		mapaImplementasaun1 = ImplementasaunPoint.objects.filter(implementasaun__statusImplementasaun="Not Start",implementasaun__is_approved=True,implementasaun__administrativepost__id=postuData.id).all()
		mapaImplementasaun2 = ImplementasaunPoint.objects.filter(implementasaun__statusImplementasaun="On Going",implementasaun__is_approved=True,implementasaun__administrativepost__id=postuData.id).all()
		mapaImplementasaun3 = ImplementasaunPoint.objects.filter(implementasaun__statusImplementasaun="Pending",implementasaun__is_approved=True,implementasaun__administrativepost__id=postuData.id).all()
		mapaImplementasaun4 = ImplementasaunPoint.objects.filter(implementasaun__statusImplementasaun="Abandone",implementasaun__is_approved=True,implementasaun__administrativepost__id=postuData.id).all()
		mapaImplementasaun5 = ImplementasaunPoint.objects.filter(implementasaun__statusImplementasaun="Complate",implementasaun__is_approved=True,implementasaun__administrativepost__id=postuData.id).all()
		rightData = Village.objects.filter(administrativepost__id=postuData.id).all()
		for x in rightData.iterator():
			totalMapaImplementasaun = ImplementasaunPoint.objects.filter(implementasaun__village__id=x.id).all().count()
			rightSideObjects.append({"hashed":x.id,"name":x.name,"totData":totalMapaImplementasaun})
	context = {
		"title":f"Mapa Lokalizasaun Implementasaun Programa PNDS - Munisipiu {postuData.municipality}, Postu {postuData.name}",
		"active_maps":"active",
		"mapaImplementasaun1":mapaImplementasaun1,
		"mapaImplementasaun2":mapaImplementasaun2,
		"mapaImplementasaun3":mapaImplementasaun3,
		"mapaImplementasaun4":mapaImplementasaun4,
		"mapaImplementasaun5":mapaImplementasaun5,
		"topSideObjects":topSideObjects,
		"rightSideObjects":rightSideObjects,
	}
	return render(request,'MapsImplementationPostu.html',context)

@login_required
@allowed_users(allowed_roles=['dir','admin','eip','fun'])
def MapaImplementasaunSuku(request, hashid):
	group = request.user.groups.all()[0].name
	sukuData = get_object_or_404(Village,id=hashid)
	programaLista = Programa.objects.all()
	topSideObjects = list()
	for x in programaLista.iterator():
		implementasaunMun = Implementasaun.objects.filter(programa__id=x.id,village__id=sukuData.id,is_approved=True).count()
		topSideObjects.append({"hashed":x.hashed,"name":x.naran,"totData":implementasaunMun})
	if group == "eip":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		mapaImplementasaun = ImplementasaunPoint.objects.filter(implementasaun__village=funsionariu.funsionariu.areavillage).all()
	if group == "fun":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		mapaImplementasaun1 = ImplementasaunPoint.objects.filter(implementasaun__statusImplementasaun="Not Start",implementasaun__village__id=sukuData.id).all()
		mapaImplementasaun2 = ImplementasaunPoint.objects.filter(implementasaun__statusImplementasaun="On Going",implementasaun__village__id=sukuData.id).all()
		mapaImplementasaun3 = ImplementasaunPoint.objects.filter(implementasaun__statusImplementasaun="Pending",implementasaun__village__id=sukuData.id).all()
		mapaImplementasaun4 = ImplementasaunPoint.objects.filter(implementasaun__statusImplementasaun="Abandone",implementasaun__village__id=sukuData.id).all()
		mapaImplementasaun5 = ImplementasaunPoint.objects.filter(implementasaun__statusImplementasaun="Complate",implementasaun__village__id=sukuData.id).all()
	if group == "admin" or group == "dir":
		mapaImplementasaun1 = ImplementasaunPoint.objects.filter(implementasaun__statusImplementasaun="Not Start",implementasaun__is_approved=True,implementasaun__village__id=sukuData.id).all()
		mapaImplementasaun2 = ImplementasaunPoint.objects.filter(implementasaun__statusImplementasaun="On Going",implementasaun__is_approved=True,implementasaun__village__id=sukuData.id).all()
		mapaImplementasaun3 = ImplementasaunPoint.objects.filter(implementasaun__statusImplementasaun="Pending",implementasaun__is_approved=True,implementasaun__village__id=sukuData.id).all()
		mapaImplementasaun4 = ImplementasaunPoint.objects.filter(implementasaun__statusImplementasaun="Abandone",implementasaun__is_approved=True,implementasaun__village__id=sukuData.id).all()
		mapaImplementasaun5 = ImplementasaunPoint.objects.filter(implementasaun__statusImplementasaun="Complate",implementasaun__is_approved=True,implementasaun__village__id=sukuData.id).all()
		rightData = Village.objects.filter(administrativepost__id=sukuData.id).all()
	context = {
		"title":f"Mapa Lokalizasaun Implementasaun Programa PNDS - Suku {sukuData.name}",
		"active_maps":"active",
		"mapaImplementasaun1":mapaImplementasaun1,
		"mapaImplementasaun2":mapaImplementasaun2,
		"mapaImplementasaun3":mapaImplementasaun3,
		"mapaImplementasaun4":mapaImplementasaun4,
		"mapaImplementasaun5":mapaImplementasaun5,
		"topSideObjects":topSideObjects,
		"sukuData":sukuData,
	}
	return render(request,'MapsImplementationSuku.html',context)


@login_required
@allowed_users(allowed_roles=['dir','admin','eip','fun'])
def MapsPrograma(request,hashid):
	group = request.user.groups.all()[0].name
	topSideObjects = Programa.objects.all()
	programaData = Programa.objects.get(hashed=hashid)
	rightSideObjects = list()
	if group == "eip":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		mapaImplementasaun = ImplementasaunPoint.objects.filter(implementasaun__village=funsionariu.funsionariu.areavillage).all()
		rightData = Municipality.objects.all()
		for x in rightData.iterator():
			totalMapaImplementasaun = ImplementasaunPoint.objects.filter(implementasaun__municipality__id=x.id).all().count()
			rightSideObjects.append({"hashed":x.id,"name":x.name,"totData":totalMapaImplementasaun})
	if group == "fun":
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		mapaImplementasaun1 = ImplementasaunPoint.objects.filter(implementasaun__programa=programaData.id,implementasaun__statusImplementasaun="Not Start",implementasaun__administrativepost__id=funsionariu.funsionariu.areaadministrativepost.id).all()
		mapaImplementasaun2 = ImplementasaunPoint.objects.filter(implementasaun__programa=programaData.id,implementasaun__statusImplementasaun="On Going",implementasaun__administrativepost__id=funsionariu.funsionariu.areaadministrativepost.id).all()
		mapaImplementasaun3 = ImplementasaunPoint.objects.filter(implementasaun__programa=programaData.id,implementasaun__statusImplementasaun="Pending",implementasaun__administrativepost__id=funsionariu.funsionariu.areaadministrativepost.id).all()
		mapaImplementasaun4 = ImplementasaunPoint.objects.filter(implementasaun__programa=programaData.id,implementasaun__statusImplementasaun="Abandone",implementasaun__administrativepost__id=funsionariu.funsionariu.areaadministrativepost.id).all()
		mapaImplementasaun5 = ImplementasaunPoint.objects.filter(implementasaun__programa=programaData.id,implementasaun__statusImplementasaun="Complate",implementasaun__administrativepost__id=funsionariu.funsionariu.areaadministrativepost.id).all()
		rightData = Village.objects.filter(administrativepost__id=funsionariu.funsionariu.areaadministrativepost.id).all()
		for x in rightData.iterator():
			totalMapaImplementasaun = ImplementasaunPoint.objects.filter(implementasaun__village__id=x.id).all().count()
			rightSideObjects.append({"hashed":x.id,"name":x.name,"totData":totalMapaImplementasaun})
	if group == "admin" or group == "dir":
		mapaImplementasaun1 = ImplementasaunPoint.objects.filter(implementasaun__programa=programaData.id,implementasaun__statusImplementasaun="Not Start",implementasaun__is_approved=True).all()
		mapaImplementasaun2 = ImplementasaunPoint.objects.filter(implementasaun__programa=programaData.id,implementasaun__statusImplementasaun="On Going",implementasaun__is_approved=True).all()
		mapaImplementasaun3 = ImplementasaunPoint.objects.filter(implementasaun__programa=programaData.id,implementasaun__statusImplementasaun="Pending",implementasaun__is_approved=True).all()
		mapaImplementasaun4 = ImplementasaunPoint.objects.filter(implementasaun__programa=programaData.id,implementasaun__statusImplementasaun="Abandone",implementasaun__is_approved=True).all()
		mapaImplementasaun5 = ImplementasaunPoint.objects.filter(implementasaun__programa=programaData.id,implementasaun__statusImplementasaun="Complate",implementasaun__is_approved=True).all()
		rightData = Municipality.objects.all()
		for x in rightData.iterator():
			totalMapaImplementasaun = ImplementasaunPoint.objects.filter(implementasaun__municipality__id=x.id).all().count()
			rightSideObjects.append({"hashed":x.id,"name":x.name,"totData":totalMapaImplementasaun})
	context = {
		"title":f"Mapa Lokalizasaun Implementasaun Programa PNDS",
		"active_maps":"active",
		"mapaImplementasaun1":mapaImplementasaun1,
		"mapaImplementasaun2":mapaImplementasaun2,
		"mapaImplementasaun3":mapaImplementasaun3,
		"mapaImplementasaun4":mapaImplementasaun4,
		"mapaImplementasaun5":mapaImplementasaun5,
		"topSideObjects":topSideObjects,
		"rightSideObjects":rightSideObjects,
	}
	return render(request,'dashMaps.html',context)
