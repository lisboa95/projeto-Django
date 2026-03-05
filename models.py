from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome do Curso")
    descricao = models.TextField(verbose_name="Descrição")
    carga_horaria = models.IntegerField(verbose_name="Carga Horária (horas)")
    data_inicio = models.DateField(verbose_name="Data de Início")
    data_termino = models.DateField(verbose_name="Data de Término")
    ativo = models.BooleanField(default=True, verbose_name="Ativo?")
    criado_em = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Usuário")
    cpf = models.CharField(max_length=14, unique=True, verbose_name="CPF")
    telefone = models.CharField(max_length=20, verbose_name="Telefone")
    data_nascimento = models.DateField(verbose_name="Data de Nascimento")
    criado_em = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.get_full_name() or self.user.username
    
    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"

class Matricula(models.Model):
    STATUS_CHOICES = [
        ('ativa', 'Ativa'),
        ('concluida', 'Concluída'),
        ('cancelada', 'Cancelada'),
    ]
    
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, verbose_name="Aluno")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    data_matricula = models.DateTimeField(auto_now_add=True, verbose_name="Data da Matrícula")
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='ativa',
        verbose_name="Status"
    )
    nota_final = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        null=True, 
        blank=True,
        verbose_name="Nota Final"
    )
    
    class Meta:
        verbose_name = "Matrícula"
        verbose_name_plural = "Matrículas"
        unique_together = ['aluno', 'curso']
    
    def __str__(self):
        return f"{self.aluno} - {self.curso}"