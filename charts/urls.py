from django.urls import path
from . import views
urlpatterns = [
	path('chart-sumariu-programa/',views.ChartSumariuPrograma,name='ChartSumariuPrograma'),
	path('chart-status-implementasaun-programa/',views.ChartStatusImplementasaunPrograma,name='ChartStatusImplementasaunPrograma'),
	path('chart-area-implementasaun-programa/',views.ChartImplementasaunProgramaArea,name='ChartImplementasaunProgramaArea'),
	path('chart-tinan-implementasaun-programa/',views.ChartImplementasaunProgramaYear,name='ChartImplementasaunProgramaYear'),
]