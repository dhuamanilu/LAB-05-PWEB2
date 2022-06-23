from django import forms

from .models import Persona

class PersonaForm(forms.ModelForm):
	class Meta:
		model = Persona
		fields=[
			'nombres',
			'apellidos',
			'edad',
			'donador',
		]

class RawPersonaForm(forms.Form):
	nombres = forms.CharField(
		widget = forms.Textarea(
			attrs ={'Placeholder': 'Solo tu nombre por favor',
			'id':'nombreID',
			'class':'special',
			'cols':'10',
			} 
		)
	)
	apellidos= forms.CharField()
	edad=forms.IntegerField(initial = 20)
	donador=forms.BooleanField(label_suffix="====")