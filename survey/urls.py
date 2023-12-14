from django.urls import path
from . import views

urlpatterns = [
	path('lista-Survey/',views.ListaSurvey,name="ListaSurvey"),
	path('rejista-Survey/',views.AddSurvey,name="AddSurvey"),
	path('altera-Survey/<str:hashid>/<str:page>',views.UpdateSurvey,name="UpdateSurvey"),
	path('xave-dadus-Survey/<str:hashid>/<str:page>',views.lockSurveyData,name="lockSurveyData"),
	path('loke-dadus-Survey/<str:hashid>/<str:page>',views.unlockSurveyData,name="unlockSurveyData"),
	path('manda-dadus-Survey/<str:hashid>/<str:page>',views.mandaSurveyData,name="mandaSurveyData"),
	path('detallu-dadus-Survey/<str:hashid>',views.detalluSurveyData,name="detalluSurveyData"),
]