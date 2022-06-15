from django import forms

from .models import Persona

class PersonaForm(forms.modelForm):
	class Meta:
		model = Persona
		fields=[
			'nombres',
			'apellidos',
			'edad',
			'donador'
		]