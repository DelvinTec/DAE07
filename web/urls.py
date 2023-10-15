from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.AlumnoView.as_view(), name='index'),
    path('/index1', views.ProfesorView.as_view(), name='index1'),
    path('eliminacionAlumno/<int:id>/', views.eliminar_alumno, name='eliminar_alumno'),
    path('eliminacionProfesor/<int:id>/', views.eliminar_profesor, name='eliminar_profesor'),
]
