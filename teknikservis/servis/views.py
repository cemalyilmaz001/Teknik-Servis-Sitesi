from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Data, Ayarlar
from django.contrib import auth
import datetime
# Create your views here.

def login(request):
	if request.method == "POST":
		user = authenticate(username = request.POST['username'], password = request.POST['password'])

		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			return redirect('/login')
	else:
		return render(request, "login.html")


def logout_view(request):
	logout(request)
	return redirect('/')


def teknik_main(request):
	context= {"ayar":Ayarlar.objects.all()}
	return render(request, "teknik.html",context)

def settings(request):
	if request.method == 'POST':
		kullanici  = request.POST["kullanici"]
		sirketname = request.POST["sirketname"]
		telefon    = request.POST["telefon"]
		mail       = request.POST["mail"]
		l = 0
		user = User.objects.get(id=request.user.id)

		for i in Ayarlar.objects.all():
			if i.usernameqv != kullanici:
				if len(kullanici) == 0:
					pass
				else:
					user.username = kullanici
					i.usernameqv = kullanici
					l += 1

			if i.şrkt_name != sirketname:
				if len(sirketname) == 0:
					pass
				else:
					i.şrkt_name = sirketname
					l += 1

			if i.şrkt_tel != telefon:
				if len(telefon) == 0:
					pass
				else:
					i.şrkt_tel = telefon
					l += 1

			if i.şrkt_email != mail:
				if len(mail) == 0:
					pass
				else:
					i.şrkt_email = mail
					l += 1

			user.save()
			i.save()

		if l == 5:
			setting = Ayarlar.objects.create(usernameqv=kullanici, şrkt_name=sirketname, şrkt_tel=telefon, şrkt_email=mail)
			setting.save()

		messages.success(request, f'Kayıt Başarılı !!')
		return redirect("/ayarlar")

	else:
		context= {"ayar":Ayarlar.objects.all()}
		return render(request, "settings.html",context)
	

def parola(request):
	if request.method == "POST":  
		if (request.POST['mevcut'] and request.POST['parola'] and  request.POST['parola2']):
			mevcutparola        = request.POST['mevcut']
			yeniparola          = request.POST['parola']
			yeniparolatekrar    = request.POST['parola2']
			username = auth.get_user(request)
			user = authenticate(username=username, password=mevcutparola)
			if user is not None:
				if (yeniparola == yeniparolatekrar):
					u = User.objects.get(username=username)
					u.set_password(yeniparolatekrar)
					u.save()
					messages.add_message(request, messages.SUCCESS, 'Parolanız Güncellenmiştir.')
					return redirect('/login')
				else:
					messages.add_message(request, messages.ERROR, 'Yeni Parola Hatası.')
					return redirect('/parola-güncelle')
			else:
				messages.add_message(request, messages.ERROR, 'Mevcut Parola Hatası.')
				return redirect('/parola-güncelle')

			return redirect('/parola-güncelle')    
	else:
		context= {"ayar":Ayarlar.objects.all()}
		return render(request, "parola.html",context)
