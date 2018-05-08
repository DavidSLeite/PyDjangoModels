from django.shortcuts import render

def index(request):
	return render(request, 'portal/index.html')
	
def login(request):
	if request.method == 'GET':
		return render(request, 'portal/login.html')
	else:
		print("Acesso Via POST")
		if request.POST.get('senha') == 'teste123':
			print("O Usuario", request.POST.get('email'), "entrou com sucesso")
			return render(request, 'portal/index.html')
		else:
			print("O Usuario", request.POST.get('email'), "Digitou a Senha errada")
			return render(request, 'portal/login.html')
	
def alunos(request):
	if request.method == 'GET':
		return render(request, 'portal/alunos.html')
	else:
		return render(request, 'portal/alunos.html')
		
def novo_aluno(request):
	if request.method == 'GET':
		return render(request, 'portal/novo_aluno.html')
	else:
		return render(request, 'portal/novo_aluno.html')
		
def detalhe_aluno(request):
	if request.method == 'GET':
		return render(request, 'portal/detalhe_aluno.html')
	else:
		return render(request, 'portal/detalhe_aluno.html')
		
def curso(request):
	if request.method == 'GET':
		return render(request, 'portal/curso.html')
	else:
		return render(request, 'portal/curso.html')
		
def novo_curso(request):
	if request.method == 'GET':
		return render(request, 'portal/novo_curso.html')
	else:
		return render(request, 'portal/novo_curso.html')
		
def detalhe_curso(request):
	if request.method == 'GET':
		return render(request, 'portal/detalhe_curso.html')
	else:
		return render(request, 'portal/detalhe_curso.html')
		
def disciplinas(request):
	if request.method == 'GET':
		return render(request, 'portal/disciplinas.html')
	else:
		return render(request, 'portal/disciplinas.html')
		
def nova_disciplina(request):
	if request.method == 'GET':
		return render(request, 'portal/nova_disciplina.html')
	else:
		return render(request, 'portal/nova_disciplina.html')
		
def detalhe_disciplina(request):
	if request.method == 'GET':
		return render(request, 'portal/detalhe_disciplina.html')
	else:
		return render(request, 'portal/detalhe_disciplina.html')
		