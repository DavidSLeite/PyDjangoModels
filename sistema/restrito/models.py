from django.db import models

# Create your models here.

class AtividadeAplicacao(models.Model):
	nome_disciplina = models.CharField("nome_disciplina", max_length=60)
	semestre_ofertado = models.IntegerField("semestre_ofertado")
	ano_ofertado  = models.IntegerField("ano_ofertado")
	sequencial  = models.IntegerField("sequencial")
	data = models.DateField("data")
	titulo = models.CharField("nome_disciplina", max_length=60)
	
	def __str__(self):
		return self.nome_disciplina
		
class AtividadeVinculada(models.Model):
	ra_aluno = models.IntegerField("ra_aluno")
	nome_disciplina = models.CharField("nome_disciplina", max_length=60)
	semestre_ofertado = models.IntegerField("semestre_ofertado")
	ano_ofertado  = models.IntegerField("ano_ofertado")
	sequencial_atividade  = models.IntegerField("sequencial_atividade")
	nota = models.IntegerField("sequencial")
	
	def __str__(self):
		return self.ra_aluno
		
		
class EntregaAtividade(models.Model):
	ra_aluno = models.IntegerField("ra_aluno")
	nome_disciplina = models.CharField("nome_disciplina", max_length=60)
	ano_ofertado  = models.IntegerField("ano_ofertado")
	semestre_ofertado = models.IntegerField("semestre_ofertado")
	
	def __str__(self):
		return self.ra_aluno
		
		
class usuario(models.Model):
	ra_aluno = models.IntegerField("ra_aluno")
	senha = models.CharField("senha", max_length=20)
	
	def __str__(self):
		return self.ra_aluno