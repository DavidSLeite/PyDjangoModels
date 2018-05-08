from django.db import models

# Create your models here.
class Aluno(models.Model):
	ra = models.IntegerField("Ra")
	nome = models.CharField("Nome", max_length=60)
	email = models.CharField("Emai", max_length=60)
	
	def __str__(self):
		return self.ra