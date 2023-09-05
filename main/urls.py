from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.principal, name='principal'),
    path('contato', views.contato),
    path('index', views.pagina_inicial),
    path('area_restrita', views.area_restrita),
    path('cadastrar_pessoa', views.cadastrar),
    path('cadastrar_funcao', views.add_trabalhos, name='cad_func'),
    path('atualizacoes', views.atualizacao),
    path('consulta_cnpj', views.cnpj),
    path('atualizar_funcao', views.atualizar_funcao, name='atualizar_funcao'),
    path('atualizar_funcao/<str:id>/', views.atualizar_funcao_id, name='atualizar_funcao_id'),
    path('atualizar_pessoas', views.atualizar_cadastro, name='atualizar_cadastro'),
    path('atualizar_pessoas/<str:id>/', views.atualizar_cadastro_id, name='atualizar_cadastro_id'),
    path('atualizacao_realizada', views.atualizacao_realizada),
    path('cadastro_realizado', views.cadastro_realizado),
    path('foto', views.foto, name='carregar_foto'),
    path('mapa', views.mapa, name='mapa')
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)