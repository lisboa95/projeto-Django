"""
URL configuration for gestao_cursos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from cursos.views import home, dashboard, perfil_aluno

urlpatterns = [
    # Painel administrativo do Django
    path('admin/', admin.site.urls),
    
    # Página inicial do sistema
    path('', home, name='home'),
    
    # URLs do app cursos (rotas públicas)
    path('cursos/', include('cursos.urls')),
    
    # Dashboard do sistema (requer autenticação)
    path('dashboard/', dashboard, name='dashboard'),
    
    # Perfil do aluno (requer autenticação)
    path('perfil/', perfil_aluno, name='perfil_aluno'),
    
    # Sistema de autenticação
    path('login/', auth_views.LoginView.as_view(
        template_name='auth/login.html',
        redirect_authenticated_user=True,  # Redireciona se já estiver logado
        extra_context={
            'next': '/dashboard/',  # Para onde vai após login
        }
    ), name='login'),
    
    # Logout do sistema
    path('logout/', auth_views.LogoutView.as_view(
        next_page='home'  # Para onde vai após logout
    ), name='logout'),
    
    # URLs de alteração de senha (opcional - para versões futuras)
    # path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

# Configurações adicionais para o admin
admin.site.site_header = 'Sistema de Gestão de Cursos - Administração'
admin.site.site_title = 'Gestão de Cursos'
admin.site.index_title = 'Painel de Controle'