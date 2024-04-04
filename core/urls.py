from django.urls import path
from .views import home, pesquisar, atualizar, deletar, criar
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('pesquisar/', pesquisar, name='pesquisar'),
    path('atualizar/<int:usuario_id>/', views.atualizar, name='atualizar'),
    path('deletar/', deletar, name='deletar'),
    path('criar/', criar, name='criar'),
]
