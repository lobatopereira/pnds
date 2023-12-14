from django.urls import path
from . import views

urlpatterns = [
	path('Formulariu-Monitoring-Implementasaun-Programa/<str:hashid>',views.addMonitoringImplementasaun,name="addMonitoringImplementasaun"),
	path('Formulariu-Altera-Monitoring-Implementasaun-Programa/<str:hashid>/<str:page>',views.updateMonitoringImplementasaun,name="updateMonitoringImplementasaun"),
	path('Xave-Monitoring-Implementasaun-Programa/<str:hashid>/<str:page>',views.lockMonitoringImplementasaunPrograma,name="lockMonitoringImplementasaunPrograma"),
	path('Loke-Monitoring-Implementasaun-Programa/<str:hashid>/<str:page>',views.unlockMonitoringImplementasaunPrograma,name="unlockMonitoringImplementasaunPrograma"),
	path('Manda-Dadus-Monitoring-Implementasaun-Programa/<str:hashid>/<str:page>',views.mandaMonitoringImplementasaunPrograma,name="mandaMonitoringImplementasaunPrograma"),
	
	path('Formulariu-Monitoring-Post-Implementasaun-Programa/<str:hashid>',views.addPostMonitoringImplementasaun,name="addPostMonitoringImplementasaun"),
	path('Formulariu-Altera-Monitoring-Post-Implementasaun-Programa/<str:hashid>/<str:page>',views.updateMonitoringPostImplementasaun,name="updateMonitoringPostImplementasaun"),
	path('Xave-Monitoring-Post-Implementasaun-Programa/<str:hashid>/<str:page>',views.lockMonitoringPostImplementasaunPrograma,name="lockMonitoringPostImplementasaunPrograma"),
	path('Loke-Monitoring-Post-Implementasaun-Programa/<str:hashid>/<str:page>',views.unlockMonitoringPostImplementasaunPrograma,name="unlockMonitoringPostImplementasaunPrograma"),
	path('Manda-Dadus-Monitoring-Post-Implementasaun-Programa/<str:hashid>/<str:page>',views.mandaMonitoringPostImplementasaunPrograma,name="mandaMonitoringPostImplementasaunPrograma"),
]