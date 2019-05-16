from django.shortcuts import render, redirect, HttpResponse
from .models import Aluno_Diciplina, Aluno, Aluno_Diciplina, Turma, Diciplina
from django.contrib.auth import authenticate, login as dj_login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from .forms import FormAluno, FormAluno_Diciplina
from django.template.context import RequestContext
import json

# Create your views here.
def calcMedia(request):
	alunos = Aluno_Diciplina.objects.all()
	for aluno in alunos:
		aluno.calcular_media()
		aluno.definir_situacao()
	return redirect('/admin/lanc_notas/aluno_diciplina/')

@login_required(login_url='/login') #verifica o usuario
def index(request):
	alunos = Aluno.objects.all() 
	alunosAp = Aluno_Diciplina.objects.filter(situacao='Aprovado')
	alunosRec = Aluno_Diciplina.objects.filter(situacao='Recuperação')
	alunosRep = Aluno_Diciplina.objects.filter(situacao='Reprovado')

	#print(request.get_full_path())
	pagina = str(request.get_full_path())
	aux = pagina.split('/')
	print(aux)

	#prototipo
	diciplinas = Diciplina.objects
	alunos = Aluno_Diciplina.objects
	lista = [str(aluno.diciplina) for aluno in alunos.filter(situacao='Aprovado')]
	lista_diciplinas = [dici.nome_diciplina for dici in diciplinas.all()] #pega todas as diciplinas
	dados = [[li, lista.count(li)] for li in lista_diciplinas]
	dados = dict(dados) #{'Calculo I': 4, 'Tecnologia Web': 5, 'Programação Orientada a Objeto': 2}

	names = [dici for dici in dados.keys()]
	#prices = [obj. for obj in alunoBd]
	prices = [qtd for qtd in dados.values()]
	#reprov = [arped, arbd, arpoo, arcalc]
	#recup = [aerped, aerpbd, aerpoo, aercalc]

	context = {
	  'alunos': alunos,
	  'pagina': pagina,
	  'alunosAp': alunosAp,
	  'alunosRec': alunosRec,
	  'alunosRep': alunosRep,
	  'names': json.dumps(names),
	  'prices': json.dumps(prices),
	  #'reprov': json.dumps(reprov),
	  #'recup': json.dumps(recup),
	  #'total': alunos
	}
	print(context['names'])
	print(context['prices'])

	#print(context)
	return render(request, 'dashboard.html', context)

def clientes_ativo(request):
	print(request.get_full_path())
	pagina = str(request.get_full_path())
	return render(request, 'c_ativo.html', {'pagina': pagina})

@csrf_protect
def login(request):
	if request.POST:    
	    username = request.POST['username']
	    password = request.POST['password']
	    print(username)
	    print(password)
	    user = authenticate(username=username, password=password) #autentica o usuario
	    if user is not None: 
	    	dj_login(request, user) #loga
	    	return redirect('/dashboard') #redireciona para o dash board
	    else:
	    	return HttpResponse('<html><body><h1>Login incorreto</h1></body</html>')
	else:
		return render(request, 'login.html')

def logout_user(request):
	print(request.user)
	logout(request)
	return redirect('/login')
	
@login_required(login_url='/login') #verifica o usuario
def alunos(request):
	alunos = Aluno.objects.all()
	pagina = str(request.get_full_path())
	print(pagina)
	contexto = {
		'alunos': alunos,
		'pagina': pagina
	}
	return render(request, 'alunos.html', contexto)

@login_required(login_url='/login') #verifica o usuario
def editar(request, id):
	print(id)
	aluno = Aluno.objects.get(matricula=id)
	
	if request.POST:
		form = FormAluno(request.POST, instance=aluno) #instancia o com os dados existentes do aluno
		if form.is_valid():
			form.save()
			return redirect('/alunos/todos')
	else:
		form = FormAluno(instance=aluno)
		return render(request, 'editar.html', {'form':form})
		
@login_required(login_url='/login') #verifica o usuario
def novo(request):
	form = FormAluno(request.POST or None)
	if request.POST:
		if form.is_valid():
			form.save()
			return redirect('/alunos/todos')
	else:
		return render(request, 'novo.html', {'form':form})

@login_required(login_url='/login') #verifica o usuario
def pontuar_alunos(request):
	form = FormAluno_Diciplina(request.POST or None)
	if request.POST:
		if form.is_valid():
			form.save()
			return redirect('/alunos/todos')
	else:
		return render(request, 'novo.html', {'form':form})


@login_required(login_url='/login') #verifica o usuario
def excluir(request, id):
	print(id)
	aluno = Aluno.objects.get(pk=id)
	if request.POST:
		Aluno.objects.get(pk=id).delete()
		return redirect('/alunos/todos')
	else:
		return render(request, 'excluir.html', {'aluno':aluno})

@login_required(login_url='/login') #verifica o usuario
def alunos_aprovados(request):
	alunos = Aluno_Diciplina.objects.filter(situacao='Aprovado')
	status = 'Aprovados'
	contexto = {
		'alunos': alunos,
		'status': status
	}
	return render(request, 'a_aprovado.html', contexto)

@login_required(login_url='/login') #verifica o usuario
def alunos_reprovados(request):
	alunos = Aluno_Diciplina.objects.filter(situacao='Reprovado')
	status = 'Reprovados'
	contexto = {
		'alunos': alunos,
		'status': status
	}
	return render(request, 'a_aprovado.html', contexto)

@login_required(login_url='/login') #verifica o usuario
def alunos_recuperacao(request):
	alunos = Aluno_Diciplina.objects.filter(situacao='Recuperação')
	status = 'em Recuperação'
	contexto = {
		'alunos': alunos,
		'status': status
	}
	return render(request, 'a_aprovado.html', contexto)