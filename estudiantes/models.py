from django.db import models

# Create your models here.
class Estudiante(models.Model):
	nombres=models.CharField(max_length=40)
	apePaterno=models.CharField(max_length=40)
	apeMaterno=models.CharField(max_length=40)
	nacimiento=models.DateField()
	dni=models.CharField(max_length=8,primary_key=True)
	cui=models.CharField(max_length=8)
