from django.urls import path
from . import views

urlpatterns = [
	path("Lista-Programa/",views.ListaPrograma, name="ListaPrograma"),
	path("Adisiona-Dadus-Programa/",views.addPrograma, name="addPrograma"),
	
	path("Lista-Implementasaun-Programa/",views.ListaImplementasaun, name="ListaImplementasaun"),
	path("Mapa-Lokalizasaun-Implementasaun-Programa-Hotu-Hotu/",views.mapaLokalizasaunImplementasaunPrograma, name="mapaLokalizasaunImplementasaunPrograma"),
	path("Adisiona-Dadus-Implementasaun-Programa/",views.addImplementasaun, name="addImplementasaun"),
	path("Altera-Dadus-Implementasaun-Programa/<str:hashid>/<str:page>",views.updateImplementasaun, name="updateImplementasaun"),
	path("Detallu-Dadus-Implementasaun-Programa/<str:hashid>",views.detalluImplementasaunPrograma, name="detalluImplementasaunPrograma"),
	path("Delete-Dadus-Implementasaun-Programa/<str:hashid>",views.deleteImplementasaun, name="deleteImplementasaun"),
	path("Xave-Dadus-Implementasaun-Programa/<str:hashid>/<str:page>",views.lockImplementasaunPrograma, name="lockImplementasaunPrograma"),
	path("Loke-Dadus-Implementasaun-Programa/<str:hashid>/<str:page>",views.unlockImplementasaunPrograma, name="unlockImplementasaunPrograma"),
	path("Manda-Dadus-Implementasaun-Programa/<str:hashid>/<str:page>",views.mandaImplementasaunPrograma, name="mandaImplementasaunPrograma"),
	path("Adisiona-Dadus-Lokalizasaun-Implementasaun-Programa/<str:hashid>",views.addImplementationLocation, name="addImplementationLocation"),
	path("Update-Dadus-Lokalizasaun-Implementasaun-Programa/<str:hashid>",views.updateMapaLokalizasaunImplementasaun, name="updateMapaLokalizasaunImplementasaun"),
	
	path("Update-Status-Implementasaun-Programa/",views.updateStatusImplementasaun, name="updateStatusImplementasaun"),

	path("Lista-Implementasaun-Programa/<str:hashid>",views.listaImplementasaunPrograma, name="listaImplementasaunPrograma"),


]