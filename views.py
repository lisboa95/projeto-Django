from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Curso, Aluno, Matricula

# Página inicial do sistema
def home(request):
    return render(request, 'home_simple.html')

# Lista todos os cursos
def lista_cursos(request):
    cursos = Curso.objects.filter(ativo=True).order_by('data_inicio')
    return render(request, 'cursos/lista_cursos.html', {'cursos': cursos})

# Detalhes de um curso específico
def detalhes_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id, ativo=True)
    return render(request, 'cursos/detalhes_curso.html', {'curso': curso})

# Dashboard do sistema (apenas para usuários logados)
@login_required
def dashboard(request):
    total_cursos = Curso.objects.filter(ativo=True).count()
    total_alunos = Aluno.objects.count()
    total_matriculas = Matricula.objects.filter(status='ativa').count()
    
    # Últimos cursos adicionados
    ultimos_cursos = Curso.objects.filter(ativo=True).order_by('-criado_em')[:5]
    
    context = {
        'total_cursos': total_cursos,
        'total_alunos': total_alunos,
        'total_matriculas': total_matriculas,
        'ultimos_cursos': ultimos_cursos,
    }
    return render(request, 'cursos/dashboard.html', context)

# Perfil do aluno (apenas para o próprio aluno)
@login_required
def perfil_aluno(request):
    try:
        aluno = Aluno.objects.get(user=request.user)
        matriculas = Matricula.objects.filter(aluno=aluno)
    except Aluno.DoesNotExist:
        aluno = None
        matriculas = []
    
    context = {
        'aluno': aluno,
        'matriculas': matriculas,
    }
    return render(request, 'cursos/perfil_aluno.html', context)