from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from django.contrib.auth.models import Group,User
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from funsionariu.models import UserFunsionariu
from users.decorators import allowed_users

# Create your views here.
@login_required
@allowed_users(allowed_roles=['admin'])
def userlist(request):
	userlist = User.objects.all().exclude(is_staff=True)
	context = {
		"title":"Lista Utilizador",
		"userlist":userlist,
		"active_userlist":"active",
		"page":"userlist",
	}
	return render(request, "userlist.html",context)

@login_required
def manageAccount(request):
	group = request.user.groups.all()[0].name
	if request.method == 'POST':
		form = UserUpdateForm(request.POST, instance=request.user)
		
		if form.is_valid():
			form.save()
			messages.success(request, f'Your account has been updated!')
			return redirect('manageAccount')
	else:
		form = UserUpdateForm(instance=request.user)

	context = {
		'group':group,
		'form': form,
		'title': 'Account Info',
		'legend': 'ACCOUNT INFO',
	}
	return render(request, 'account.html', context)

@login_required
def userProfile(request):
	group = request.user.groups.all()[0].name
	profile = get_object_or_404(UserFunsionariu,id=request.user.userFunsionariu.id)
	context = {
		'group':group,
		'profile': profile,
		'title': 'Profile Utilizador',
	}
	return render(request, 'profile.html', context)

@login_required
def changeAccountPassword(request):
	group = request.user.groups.all()[0].name
	if request.method == 'POST':
		current_password = request.POST["old_password"]
		new_password = request.POST["new_password"]
		confirm_password = request.POST["confirm_password"]

		user = User.objects.get(id=request.user.id)
		un = user.username
		pwd = new_password
		check = user.check_password(current_password)
		if check==True:
			if new_password == confirm_password:
				user.set_password(new_password)
				user.save()
				authenticate(username = un, password = pwd)
				if request.user.is_authenticated:
					messages.info(request, f'Your password has been changed Successfuly!')
					return redirect('changeAccountPassword')
			else:
				messages.warning(request, f'Your New password {new_password} and Confirmation Password {confirm_password} does not match!')
				return redirect('changeAccountPassword')
		else:
			messages.warning(request, f'Your current password {current_password} is Incorrect!')
			return redirect('changeAccountPassword')

	context = {
		'group':group,
		'title': 'Change Password',
		'legend': 'CHANGE PASSWORD',
	}
	return render(request, 'changeAccountPassword.html', context)

@login_required
@allowed_users(allowed_roles=['admin'])
def resetUserPassword(request,id):
	userData = get_object_or_404(User,id=id)
	password = make_password('password')
	userData.password = password
	userData.save()
	messages.success(request, f'Password ba {userData.username} Reset ho Susesu!')
	return redirect('userlist')

@login_required
@allowed_users(allowed_roles=['admin'])
def desativuUser(request,id):
	userData = get_object_or_404(User,id=id)
	userData.is_active = False
	userData.save()
	messages.success(request, f'User {userData.username} Desativu ho Susesu!')
	return redirect('userlist')

@login_required
@allowed_users(allowed_roles=['admin'])
def ativuUser(request,id):
	userData = get_object_or_404(User,id=id)
	userData.is_active = True
	userData.save()
	messages.success(request, f'User {userData.username} Ativu ho Susesu!')
	return redirect('userlist')

@login_required
@allowed_users(allowed_roles=['admin'])
def deleteUser(request,id):
	user = get_object_or_404(User,id=id)
	user.delete()
	messages.success(request, f'Utilizador ba {user.username} Hamoos ho Susesu!')
	return redirect('userlist')