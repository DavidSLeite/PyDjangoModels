from django.urls import path
from django.contrib import admin
from sistema.views import *

urlpatterns = [
	path('', index),
	path('login', login),
	path('alunos', alunos),
	path('novo_aluno', novo_aluno),
	path('detalhe_aluno', detalhe_aluno),
	path('curso', curso),
	path('novo_curso', novo_curso),
	path('detalhe_curso', detalhe_curso),
	path('disciplinas', disciplinas),
	path('nova_disciplina', nova_disciplina),
	path('detalhe_disciplina', detalhe_disciplina),
	#path('admin/', admin.site.urls),
]