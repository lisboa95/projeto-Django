from django.contrib import admin
from .models import Curso, Aluno, Matricula

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'data_inicio', 'data_termino', 'ativo', 'carga_horaria']
    list_filter = ['ativo', 'data_inicio']
    search_fields = ['nome', 'descricao']
    list_editable = ['ativo']

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['user', 'cpf', 'telefone', 'data_nascimento']
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'cpf']

@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ['aluno', 'curso', 'status', 'nota_final', 'data_matricula']
    list_filter = ['status', 'curso', 'data_matricula']
    search_fields = ['aluno__user__username', 'curso__nome']
    list_editable = ['status', 'nota_final']