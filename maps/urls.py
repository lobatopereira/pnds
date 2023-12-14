from django.urls import path
from . import views

urlpatterns = [
	path("Dashboard-Mapa-Implementasaun-Programa/",views.DashMaps, name="DashMaps"),
	path("Mapa-Implementasaun-Programa-Munisipiu/<str:hashid>",views.MapaImplementasaunMunisipiu, name="MapaImplementasaunMunisipiu"),
	path("Mapa-Implementasaun-Programa-Postu-Administrativu/<str:hashid>",views.MapaImplementasaunPostu, name="MapaImplementasaunPostu"),
	path("Mapa-Implementasaun-Programa-Suku-Administrativu/<str:hashid>",views.MapaImplementasaunSuku, name="MapaImplementasaunSuku"),
	
	path("Mapa-Programa/<str:hashid>",views.MapsPrograma, name="MapsPrograma"),
]