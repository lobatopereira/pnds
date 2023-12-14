from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from django.contrib import messages
from funsionariu.models import Funsionariu,UserFunsionariu
from .forms import FunsionariuPostuForm,FunsionariuEIPForm,UpdateFunsionariuForm,FunsionariuDiretorForm
from django.contrib.auth.models import User,Group
from custom.utils import *
from custom.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from users.decorators import allowed_users

# Create your views here.
@login_required
@allowed_users(allowed_roles=['admin'])
def ListaFunsionariu(request):
	listaFunsionariu = Funsionariu.objects.all()
	context = {
		"title":"Lista Funsionariu PNDS",
		"active_funsionariu":"active",
		"page":"list",
		"listaFunsionariu":listaFunsionariu,
	}
	return render(request, "ListaFunsionariu.html",context)

@login_required
@allowed_users(allowed_roles=['admin'])
def AddFunsionariuPostu(request):
	if request.method == "POST":
		_, newid = getlastid(Funsionariu)
		hashid = hash_md5(str(newid))
		newid2 = getjustnewid(UserFunsionariu)
		hashid2 = hash_md5(str(newid2))
		newid3 = getjustnewid(User)
		form = FunsionariuPostuForm(request.POST,request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.hashed = hashid
			instance.user_created = request.user
			instance.tipu_f = "Fun"
			postuID = instance.areaadministrativepost
			postu = get_object_or_404(AdministrativePost,id=postuID.id)
			instance.save()
			username = str("funsionariu")+str(postu.name)+str(newid)  # funsionariu4
			password = make_password('password')
			obj2 = User(id=newid3, username=username, password=password)  # 7
			obj2.save()
			obj3 = UserFunsionariu.objects.create(user=obj2,funsionariu=instance,user_created=request.user,hashed=hashid2)
			group_user = Group.objects.get(name='fun')
			user = User.objects.get(pk=newid3)
			user.groups.add(group_user)
			messages.success(request, f'Funsionariu Postu {postu.name} Rejistu ho Susesu.')
			return redirect('ListaFunsionariu')
	else:	
		form = FunsionariuPostuForm()
	context ={
		"title":"Formulariu Rejistu Funsionariu Postu",
		"page":"form",
		"form":form,
		"active_funsionariu":"active",
	}
	return render(request,'ListaFunsionariu.html',context)

@login_required
@allowed_users(allowed_roles=['admin'])
def AddFunsionariuDiretor(request):
	if request.method == "POST":
		_, newid = getlastid(Funsionariu)
		hashid = hash_md5(str(newid))
		newid2 = getjustnewid(UserFunsionariu)
		hashid2 = hash_md5(str(newid2))
		newid3 = getjustnewid(User)
		form = FunsionariuDiretorForm(request.POST,request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.hashed = hashid
			instance.user_created = request.user
			instance.tipu_f = "Dir"
			instance.save()
			username = str("diretor")+str(newid)  # funsionariu4
			password = make_password('password')
			obj2 = User(id=newid3, username=username, password=password)  # 7
			obj2.save()
			obj3 = UserFunsionariu.objects.create(user=obj2,funsionariu=instance,user_created=request.user,hashed=hashid2)
			group_user = Group.objects.get(name='dir')
			user = User.objects.get(pk=newid3)
			user.groups.add(group_user)
			messages.success(request, f'Dadus Diretor Rejistu ho Susesu.')
			return redirect('ListaFunsionariu')
	else:	
		form = FunsionariuDiretorForm()
	context ={
		"title":"Formulariu Rejistu Dadus Diretor",
		"page":"form",
		"form":form,
		"active_funsionariu":"active",
	}
	return render(request,'ListaFunsionariu.html',context)

@login_required
@allowed_users(allowed_roles=['admin'])
def AddFunsionariuEIP(request):
	if request.method == "POST":
		_, newid = getlastid(Funsionariu)
		hashid = hash_md5(str(newid))
		newid2 = getjustnewid(UserFunsionariu)
		hashid2 = hash_md5(str(newid2))
		newid3 = getjustnewid(User)
		form = FunsionariuEIPForm(request.POST,request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.hashed = hashid
			instance.user_created = request.user
			instance.tipu_f = "EIP"
			sukuID = instance.areavillage
			suku = get_object_or_404(Village,id=sukuID.id)
			instance.save()
			username = str("eip")+str(suku.name)+str(newid)  # funsionariu4
			password = make_password('password')
			obj2 = User(id=newid3, username=username, password=password)  # 7
			obj2.save()
			obj3 = UserFunsionariu.objects.create(user=obj2,funsionariu=instance,user_created=request.user,hashed=hashid2)
			group_user = Group.objects.get(name='eip')
			user = User.objects.get(pk=newid3)
			user.groups.add(group_user)
			messages.success(request, f'Funsionariu EIP {suku.name} Rejistu ho Susesu.')
			return redirect('ListaFunsionariu')
	else:	
		form = FunsionariuEIPForm()
	context ={
		"title":"Formulariu Rejistu Funsionariu EIP",
		"page":"form",
		"form":form,
		"active_funsionariu":"active",
	}
	return render(request,'ListaFunsionariu.html',context)

# @login_required
# @allowed_users(allowed_roles=['admin'])
# def AddFunsionariu(request):
# 	if request.method == "POST":
# 		_, newid = getlastid(Funsionariu)
# 		hashid = hash_md5(str(newid))
# 		newid2 = getjustnewid(UserFunsionariu)
# 		hashid2 = hash_md5(str(newid2))
# 		newid3 = getjustnewid(User)
# 		form = FunsionariuForm(request.POST,request.FILES)
# 		if form.is_valid():
# 			instance = form.save(commit=False)
# 			instance.hashed = hashid
# 			instance.user_created = request.user
# 			instance.save()
# 			if tipu_user == "Dir":
# 				username = str("diretor")+str(newid)  # funsionariu4
# 			else:
# 				username = str("funsionariu")+str(newid)  # funsionariu4
# 			password = make_password('password')
# 			obj2 = User(id=newid3, username=username, password=password)  # 7
# 			obj2.save()
# 			obj3 = UserFunsionariu.objects.create(user=obj2,funsionariu=instance,user_created=request.user,hashed=hashid2)
# 			tipu_user = form.cleaned_data.get('tipu_f')
# 			if tipu_user == "EIP":
# 				group_user = Group.objects.get(name='eip')
# 			elif tipu_user == "Dir":
# 				group_user = Group.objects.get(name='dir')
# 			else :
# 				group_user = Group.objects.get(name='fun')
# 			user = User.objects.get(pk=newid3)
# 			user.groups.add(group_user)
# 			messages.success(request, f'Funsionariu Rejistu ho Susesu.')
# 			return redirect('ListaFunsionariu')
# 	else:	
# 		form = FunsionariuForm()
# 	context ={
# 		"title":"Formulariu Rejistu Funsionariu",
# 		"page":"form",
# 		"form":form,
# 		"active_funsionariu":"active",
# 	}
# 	return render(request,'ListaFunsionariu.html',context)

@login_required
@allowed_users(allowed_roles=['admin'])
def UpdateFunsionariu(request,hashid):
	funsionariu = get_object_or_404(Funsionariu,hashed=hashid)
	if request.method == "POST":
		newid2 = getjustnewid(UserFunsionariu)
		hashid2 = hash_md5(str(newid2))
		newid3 = getjustnewid(User)
		form = UpdateFunsionariuForm(request.POST,request.FILES,instance=funsionariu)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			messages.success(request, f'Dadus Funsionariu Altera ho Susesu.')
			return redirect('ListaFunsionariu')
	else:	
		form = UpdateFunsionariuForm(instance=funsionariu)
	context ={
		"title":"Formulariu Altera Dadus Funsionariu",
		"page":"form",
		"form":form,
		"active_funsionariu":"active",
	}
	return render(request,'ListaFunsionariu.html',context)