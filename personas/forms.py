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
	donador=forms.BooleanField(label_suffix="==")

	def clean_nombres(self,*args,**kwargs):
		print('paso')
		name=self.cleaned_data.get('nombres')
		
		if name[0:1].isupper():
			if len(name) > 100 :
				raise forms.ValidationError('Su nombre debe de tener menos de 100 caracteres')
			else:	
				return name
		else:
			raise forms.ValidationError('La primera letra en mayúscula')

	def clean_apellidos(self,*args,**kwargs):
		print('paso a limpieza apellidos')
		apell=self.cleaned_data.get('apellidos')
		if apell[0:1].isupper():
			if len(apell) > 100 :
				raise forms.ValidationError('Su apellido debe de tener menos de 100 caracteres')
			else:
				return apell
		else:
			raise forms.ValidationError('La primera letra en mayúscula')

	def clean_edad(self,*args,**kwargs):
		print('paso a limpieza edad')
		eda=self.cleaned_data.get('edad')
		if eda > 400 or eda < 0:
			raise forms.ValidationError('Su edad debe de estar entre 0 y 400')
		else:
			return eda