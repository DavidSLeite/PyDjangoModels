from django.db import models

# Create your models here.
class Disciplica(models.Model):
	nome = models.CharField("Nome", max_length=60)
	ementa = models.TextField("Ementa")
	
	def __str__(self):
		return self.nome
		
class DisciplinaOfertada(models.Model):
	nome_disciplina = models.CharField("Nome", max_length=60)
	ano = models.IntegerField("Ano")
	semestre = models.IntegerField("Semestre")
	
	def __str__(self):
		return self.nome_disciplina