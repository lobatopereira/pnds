from django.urls import path
from . import views


urlpatterns = [
	path('lista-Funsionariu/',views.ListaFunsionariu,name="ListaFunsionariu"),
	path('adisiona-Funsionariu-Postu/',views.AddFunsionariuPostu,name="AddFunsionariuPostu"),
	path('adisiona-Funsionariu-EIP/',views.AddFunsionariuEIP,name="AddFunsionariuEIP"),
	path('adisiona-Funsionariu-Diretor/',views.AddFunsionariuDiretor,name="AddFunsionariuDiretor"),
	path('altera-dadus-Funsionariu/<str:hashid>',views.UpdateFunsionariu,name="UpdateFunsionariu"),
]