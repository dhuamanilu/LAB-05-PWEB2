from django.shortcuts import render
from .models import Persona
# Create your views here.
def personaTestView(request):
	obj =Persona.objects.get(id=2)
	context={
		'objeto':obj,	
	}
	return render (request,'personas/descripcion.html',context)

def personaCreateView(request):
	form = PersonaForm(request.POST or None)
	is form.is_valid():
		form.save()
		form=PersonaForm()
	context={
		'form':form,
	}
	return render(request,'personas/personasCreate.html',context)