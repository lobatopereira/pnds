from django.urls import path
from . import views

urlpatterns = [
	path('badge/', views.APINotifBadge.as_view()),
	path('survey/', views.APINotifSurvey.as_view()),
	path('implementasaun/', views.APINotifImplementasaun.as_view()),
	path('monitoring-implementasaun/', views.APINotifMonitoringImplementasaun.as_view()),
	path('monitoring-post-implementasaun/', views.APINotifMonitoringPostImplementasaun.as_view()),
	
	path('badge-rejected/', views.APINotifBadgeRejected.as_view()),
	path('survey-rejeitadu/', views.APINotifSurveyRejected.as_view()),
	path('implementasaun-rejeitadu/', views.APINotifImplementasaunRejected.as_view()),
	path('monitoring-implementasaun-rejeitadu/', views.APINotifImplementationMonitoringRejected.as_view()),
	path('monitoring-post-implementasaun-rejeitadu/', views.APINotifPostImplementationMonitoringRejected.as_view()),
]