from django.urls import path
from .views import home, pesquisar, atualizar, deletar, criar
from . import views
from .views import atualizar

urlpatterns = [
    path('', home, name='home'),
    path('pesquisar/', pesquisar, name='pesquisar'),
    path('atualizar/', views.nova_view, name='atualizar'),
    path('atualizar/<int:usuario_id>/', views.atualizar, name='atualizar_id'),
    path('deletar/', deletar, name='deletar'),
    path('criar/', criar, name='criar'),
]
