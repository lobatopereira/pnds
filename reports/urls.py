from django.urls import path
from . import views,r_views

urlpatterns = [
	path('Dashboard-Relatoriu-Tabular/',views.DashTabularReport,name="DashTabularReport"),
	
	path('Relatoriu-Survey-Aprovadu/',r_views.ReportAllAprovedSurvey,name="ReportAllAprovedSurvey"),
	
	path('Relatoriu-Implementasaun-Aprovadu/',r_views.ReportAllAprovedImplementation,name="ReportAllAprovedImplementation"),
	path('Relatoriu-Implementasaun-Programa/<str:hashid>',r_views.ReportImplementasaunPrograma,name="ReportImplementasaunPrograma"),
	path('Relatoriu-Status-Implementasaun-Programa/<str:hashidProgram>/<str:status>',r_views.ReportStatusImplementasaunPrograma,name="ReportStatusImplementasaunPrograma"),
	path('Relatoriu-Tinan-Implementasaun-Programa/<str:tinan>/<str:hashidProgram>',r_views.ReportTinanImplementasaunPrograma,name="ReportTinanImplementasaunPrograma"),
	path('Relatoriu-Suku-Implementasaun-Programa/<str:hashidProgram>/<str:suku>',r_views.ReportSukuImplementasaunPrograma,name="ReportSukuImplementasaunPrograma"),
	path('Relatoriu-Munisipiu-Implementasaun-Programa/<str:hashidProgram>/<str:munisipiu>',r_views.ReportMunisipiuImplementasaunPrograma,name="ReportMunisipiuImplementasaunPrograma"),
	

	path('Dashboard-Relatoriu-Grafiku/',views.DashGraphReport,name="DashGraphReport"),

]