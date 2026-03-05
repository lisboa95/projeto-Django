import os
import django
from datetime import date, timedelta

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestao_cursos.settings')
django.setup()

from django.contrib.auth.models import User
from cursos.models import Curso, Aluno, Matricula

def criar_dados():
    print("🎯 CRIANDO DADOS DE TESTE...")
    
    # 1. Criar cursos
    cursos_data = [
        {
            'nome': 'Python para Iniciantes',
            'descricao': 'Curso introdutório de programação Python com foco em lógica e algoritmos.',
            'carga_horaria': 40,
            'data_inicio': date(2024, 3, 1),
            'data_termino': date(2024, 4, 10),
        },
        {
            'nome': 'Desenvolvimento Web com Django',
            'descricao': 'Aprenda a criar aplicações web completas usando Django framework.',
            'carga_horaria': 60,
            'data_inicio': date(2024, 4, 1),
            'data_termino': date(2024, 6, 1),
        },
        {
            'nome': 'Banco de Dados SQL',
            'descricao': 'Fundamentos de banco de dados relacionais e linguagem SQL.',
            'carga_horaria': 50,
            'data_inicio': date(2024, 5, 1),
            'data_termino': date(2024, 7, 1),
        },
        {
            'nome': 'JavaScript Moderno',
            'descricao': 'Desenvolvimento front-end com JavaScript ES6+, React e Node.js.',
            'carga_horaria': 80,
            'data_inicio': date(2024, 6, 1),
            'data_termino': date(2024, 9, 1),
        },
    ]
    
    cursos_criados = []
    for dados in cursos_data:
        curso, created = Curso.objects.get_or_create(
            nome=dados['nome'],
            defaults=dados
        )
        if created:
            cursos_criados.append(curso)
            print(f"✅ Curso criado: {curso.nome}")
    
    # 2. Criar alunos (se não existirem)
    alunos_data = [
        {'username': 'maria.silva', 'nome': 'Maria', 'sobrenome': 'Silva', 'cpf': '111.222.333-44'},
        {'username': 'joao.santos', 'nome': 'João', 'sobrenome': 'Santos', 'cpf': '222.333.444-55'},
        {'username': 'ana.pereira', 'nome': 'Ana', 'sobrenome': 'Pereira', 'cpf': '333.444.555-66'},
        {'username': 'carlos.oliveira', 'nome': 'Carlos', 'sobrenome': 'Oliveira', 'cpf': '444.555.666-77'},
    ]
    
    alunos_criados = []
    for dados in alunos_data:
        # Criar usuário se não existir
        user, user_created = User.objects.get_or_create(
            username=dados['username'],
            defaults={
                'first_name': dados['nome'],
                'last_name': dados['sobrenome'],
                'email': f"{dados['username']}@email.com",
            }
        )
        
        if user_created:
            user.set_password('senha123')  # Senha padrão
            user.save()
        
        # Criar aluno se não existir
        aluno, aluno_created = Aluno.objects.get_or_create(
            user=user,
            defaults={
                'cpf': dados['cpf'],
                'telefone': '(11) 99999-8888',
                'data_nascimento': date(1995, 1, 1),
            }
        )
        
        if aluno_created or user_created:
            alunos_criados.append(aluno)
            print(f"✅ Aluno criado: {aluno.user.get_full_name()} ({aluno.user.username})")
    
    # 3. Criar matrículas de teste
    if cursos_criados and alunos_criados:
        status_options = ['ativa', 'concluida', 'cancelada']
        
        for i, aluno in enumerate(alunos_criados):
            for j, curso in enumerate(cursos_criados):
                if (i + j) % 2 == 0:  # Matrícula condicional
                    matricula, created = Matricula.objects.get_or_create(
                        aluno=aluno,
                        curso=curso,
                        defaults={
                            'status': status_options[(i + j) % len(status_options)],
                            'nota_final': (i + j + 6) * 1.5,  # Nota fictícia
                        }
                    )
                    if created:
                        print(f"✅ Matrícula criada: {aluno} → {curso}")
    
    print("\n" + "="*50)
    print("🎊 DADOS DE TESTE CRIADOS COM SUCESSO!")
    print("="*50)
    print(f"📚 Cursos: {Curso.objects.count()}")
    print(f"👥 Alunos: {Aluno.objects.count()}")
    print(f"📋 Matrículas: {Matricula.objects.count()}")
    print("\n🔑 CREDENCIAIS PARA TESTE:")
    print("-" * 30)
    for aluno in Aluno.objects.all()[:3]:
        print(f"Usuário: {aluno.user.username} | Senha: senha123")
    print("\n🌐 ACESSE:")
    print(f"Home: http://127.0.0.1:8000/")
    print(f"Cursos: http://127.0.0.1:8000/cursos/")
    print(f"Login: http://127.0.0.1:8000/login/")

if __name__ == '__main__':
    criar_dados()