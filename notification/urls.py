from django.urls import path
from . import views

urlpatterns = [
	path('implementation/sent',views.NotifImplementationSent,name="NotifImplementationSent"),
	path('implementation/approved/<str:hashid>/<str:page>',views.approvedImplementasaunPrograma,name="approvedImplementasaunPrograma"),
	path('implementation/reject',views.rejeitaImplementasaunPrograma,name="rejeitaImplementasaunPrograma"),
	path('detallu-implementasaun/<str:hashid>',views.detalluImplementasaunProgramaNotif,name="detalluImplementasaunProgramaNotif"),
	
	path('monitoring-implementation/sent',views.NotifMonitoringImplementationSent,name="NotifMonitoringImplementationSent"),
	path('monitoring-implementation/approved/<str:hashid>',views.approvedMonitoringImplementasaunPrograma,name="approvedMonitoringImplementasaunPrograma"),
	
	path('monitoring-post-implementation/sent',views.NotifMonitoringPostImplementationSent,name="NotifMonitoringPostImplementationSent"),
	path('monitoring-post-implementation/approved/<str:hashid>',views.approvedMonitoringPostImplementasaunPrograma,name="approvedMonitoringPostImplementasaunPrograma"),
	
	path('survey/sent',views.NotifSurveySent,name="NotifSurveySent"),
	path('survey/approved/<str:hashid>/<str:page>',views.approvedSurvey,name="approvedSurvey"),
	path('survey/rejeita/',views.rejeitaSurvey,name="rejeitaSurvey"),
	path('detallu-survey/<str:hashid>',views.detalluSurveyNotif,name="detalluSurveyNotif"),
	
	path('implementation/rejected',views.NotifImplementationReject,name="NotifImplementationReject"),
	path('survey/rejected',views.NotifSurveyReject,name="NotifSurveyReject"),
	path('monitoring-implementation/rejected',views.NotifMonitoringImplementationReject,name="NotifMonitoringImplementationReject"),
	path('monitoring-post-implementation/rejected',views.NotifMonitoringPostImplementationReject,name="NotifMonitoringPostImplementationReject"),
	
	path('monitoring-implementation-Programa/rejeita/',views.rejeitaMonitoringImplementasaunPrograma,name="rejeitaMonitoringImplementasaunPrograma"),
	path('monitoring-post-implementation-Programa/rejeita/',views.rejeitaMonitoringPostImplementasaunPrograma,name="rejeitaMonitoringPostImplementasaunPrograma"),
]	