from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count, Q
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from programa.models import Implementasaun
from monitoring.models import ImplementationMonitoring,PostImplementationMonitoring
from funsionariu.models import UserFunsionariu
from survey.models import Survey
# views here
class APINotifBadge(APIView):
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]
	def get(self, request, format=None):
		obj1 = Implementasaun.objects.filter(is_sent=True, is_approved=False).all().count()
		obj2 = ImplementationMonitoring.objects.filter(is_sent=True, is_approved=False).all().count()
		obj3 = Survey.objects.filter(is_sent=True, is_approved=False).all().count()
		obj4 = PostImplementationMonitoring.objects.filter(is_sent=True, is_approved=False).all().count()
		objects = obj1 + obj2 + obj3 + obj4
		return Response({'value':objects})

class APINotifBadgeRejected(APIView):
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]
	def get(self, request, format=None):
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		obj1 = Implementasaun.objects.filter(administrativepost=funsionariu.funsionariu.areaadministrativepost,is_sent=False, is_approved=False, is_rejected=True).all().count()
		obj2 = Survey.objects.filter(administrativepost=funsionariu.funsionariu.areaadministrativepost,is_sent=False, is_approved=False, is_rejected=True).all().count()
		obj3 = ImplementationMonitoring.objects.filter(implementasaun__administrativepost=funsionariu.funsionariu.areaadministrativepost,is_sent=False, is_approved=False, is_rejected=True).all().count()
		obj4 = PostImplementationMonitoring.objects.filter(implementasaun__administrativepost=funsionariu.funsionariu.areaadministrativepost,is_sent=False, is_approved=False, is_rejected=True).all().count()
		objects = obj1+obj2+obj3+obj4
		return Response({'value':objects})


class APINotifImplementasaun(APIView):
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]
	def get(self, request, format=None):
		objects = Implementasaun.objects.filter(is_sent=True, is_approved=False).all().count()
		return Response({'value':objects})

class APINotifSurvey(APIView):
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]
	def get(self, request, format=None):
		objects = Survey.objects.filter(is_sent=True, is_approved=False).all().count()
		return Response({'value':objects})

class APINotifMonitoringImplementasaun(APIView):
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]
	def get(self, request, format=None):
		objects = ImplementationMonitoring.objects.filter(is_sent=True, is_approved=False).all().count()
		return Response({'value':objects})

class APINotifMonitoringPostImplementasaun(APIView):
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]
	def get(self, request, format=None):
		objects = PostImplementationMonitoring.objects.filter(is_sent=True, is_approved=False).all().count()
		return Response({'value':objects})

class APINotifImplementasaunRejected(APIView):
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]
	def get(self, request, format=None):
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		objects = Implementasaun.objects.filter(village=funsionariu.funsionariu.village,is_sent=False, is_approved=False, is_rejected=True).all().count()
		return Response({'value':objects})

class APINotifSurveyRejected(APIView):
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]
	def get(self, request, format=None):
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		objects = Survey.objects.filter(administrativepost=funsionariu.funsionariu.areaadministrativepost,is_sent=False, is_approved=False, is_rejected=True).all().count()
		return Response({'value':objects})

class APINotifImplementationMonitoringRejected(APIView):
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]
	def get(self, request, format=None):
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		objects = ImplementationMonitoring.objects.filter(implementasaun__administrativepost=funsionariu.funsionariu.areaadministrativepost,is_sent=False, is_approved=False, is_rejected=True).all().count()
		return Response({'value':objects})

class APINotifPostImplementationMonitoringRejected(APIView):
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]
	def get(self, request, format=None):
		funsionariu = get_object_or_404(UserFunsionariu,user__id=request.user.id)
		objects = PostImplementationMonitoring.objects.filter(implementasaun__administrativepost=funsionariu.funsionariu.areaadministrativepost,is_sent=False, is_approved=False, is_rejected=True).all().count()
		return Response({'value':objects})
