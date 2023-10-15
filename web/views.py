from django.shortcuts import render, redirect



# importamos la clase View
from django.views import View
from .models import *
from .forms import *



class AlumnoView(View):
    
    def get(self,request):
        listaAlumnos = TblAlumno.objects.all()
        formAlumno = AlumnoForm()
        context = {
            'alumnos' : listaAlumnos,
            'formAlumno': formAlumno
        }
        return render(request,'index.html',context)

    def post(self, request):
        formAlumno = AlumnoForm(request.POST)
        if formAlumno.is_valid():
            formAlumno.save()
            return redirect('/')
        
def eliminar_alumno(request, id):
    alumno = TblAlumno.objects.get(alumno_id=id)
    alumno.delete()
    return redirect('/')

class ProfesorView(View):
    
    def get(self,request):
        listaProfesores = TblProfesor.objects.all()
        formProfesor = ProfesorForm()
        context = {
            'profesores' : listaProfesores,
            'formProfesor': formProfesor
        }
        return render(request,'index1.html',context)

    def post(self, request):
        formProfesor = ProfesorForm(request.POST)
        if formProfesor.is_valid():
            formProfesor.save()
            return redirect('/')
        
def eliminar_profesor(request, id):
    profesor = TblProfesor.objects.get(profesor_id=id)
    profesor.delete()
    return redirect('/')

