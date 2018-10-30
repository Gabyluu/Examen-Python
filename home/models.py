from django.db import models

# Create your models here.


class Archivos_Investigacion(models.Model):
		titulo = models.CharField(max_length=32, default='Escribe el Titulo')
		autor = models.CharField(max_length=32, default='Escribe el Nombre del Autor')
		cat = (('Ciencias Computacionales','Ciencias Computacionales'),
			  ('Ciencias de la Tierra','Ciencias de la Tierra'),
			  ('Ciencias Naturales','Ciencias Naturales'),
			  ('Ciencias Sociales','Ciencias Sociales'),
			  ('Ciencias Medicas','Ciencias Medicas'))
		categoria = models.CharField(max_length=32, choices = cat, default = 'Ciencias Computacionales')

		def __str__(self):
			return self.titulo


