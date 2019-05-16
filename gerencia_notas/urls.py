"""gerencia_notas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from lanc_notas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.calcMedia),
    path('dashboard', views.index),
    path('alunos/novo', views.novo),
    path('alunos/aprovados', views.alunos_aprovados),
    path('alunos/reprovados', views.alunos_reprovados),
    path('alunos/recuperacao', views.alunos_recuperacao),
    path('alunos/todos', views.alunos),
    path('alunos/editar/<int:id>', views.editar),
    path('alunos/excluir/<int:id>', views.excluir),
    path('login', views.login),
    path('logout', views.logout_user),



]
    
