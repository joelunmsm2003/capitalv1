from django.shortcuts import *
from django.template import RequestContext
from django.contrib.auth import *
from django.contrib.auth.models import Group, User
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db.models import Max,Count
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from capital import settings
from django.db import transaction
from django.contrib.auth.hashers import *
from django.core.mail import send_mail
from django.utils.six.moves import range
from django.http import StreamingHttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.views.decorators.csrf import csrf_exempt
import time
import collections
import xlrd
import json 
import csv
import simplejson
import xlwt
import requests
import os
from PIL import Image
from resizeimage import resizeimage
from datetime import datetime,timedelta
from django.contrib.auth import authenticate
from django.contrib.sites.shortcuts import get_current_site
from app.models import *

# Prductos de un usuario

#@login_required(login_url="/autentificacion/")

def salir(request):

	logout(request)
	
	return HttpResponseRedirect("/ingresar")

def agente(request):

	id = request.user.id

	producto = Producto.objects.all()
	interes = Interes.objects.all()
	actividad = Actividad.objects.all()
	user = AuthUser.objects.get(id=id)


	if user.tipo.nombre == 'Admin':

		gestion = Gestion.objects.all()

	else:

		gestion = Gestion.objects.filter(user_id=id)

	return render(request, 'agente.html',{'producto':producto,'interes':interes,'actividad':actividad,'user':user,'gestion':gestion})


def ingresar(request):

	if request.user.is_authenticated():

		return HttpResponseRedirect("/agente")

	else:

		if request.method == 'POST':

			print request.POST

			user = request.POST['username']
			
			psw = request.POST['password']

			user = authenticate(username=user, password=psw)

		
			if user is not None:

				if user.is_active:

					login(request, user)

					return HttpResponseRedirect("/agente")

			else:

				return HttpResponseRedirect("/ingresar")
		
		else:

			return render(request, 'login.html',{})


def visita(request):

	if request.method == 'POST':

		print request.POST

		id = request.user.id

		cliente = request.POST['cliente']
		actividad= request.POST['actividad']
		interes = request.POST['interes']
		producto = request.POST['producto']
		direccion = request.POST['direccion']
		telefono = request.POST['telefono']
		fijo = request.POST['fijo']
		observacion = request.POST['observacion']

		Gestion(user_id=id,cliente=cliente,actividad_id=actividad,interes_id=interes,producto_id=producto,direccion=direccion,telefono=telefono,fijo=fijo,observacion=observacion).save()

		return HttpResponseRedirect("/agente")

	else:

		return HttpResponseRedirect("/agente")

