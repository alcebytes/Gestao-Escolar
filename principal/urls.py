from django.urls import path
from principal.views import (
	AnoLetivoNewView,
	EtapaBasicaNewView,
	AnoEscolarNewView,
	AnoLetivoListView,
	DisciplinaNewView,
	DisciplinaUpdateView,
	DisciplinaListView,
)

urlpatterns = [
	path('ano-letivo-novo/', AnoLetivoNewView.as_view(), name='ano-letivo-novo'),
	path('etapa-basica-nova/', EtapaBasicaNewView.as_view(), name='etapa-basica-nova'),
	path('ano-escolar-novo/', AnoEscolarNewView.as_view(), name='ano-escolar-novo'),
	path('anos-letivos/', AnoLetivoListView.as_view(), name='anos-letivos'),
	path('disciplina-nova/', DisciplinaNewView.as_view(), name='disciplina-nova'),
	path('<int:pk>/alterar', DisciplinaUpdateView.as_view(), name='disciplina-update'),
	path('disciplinas/', DisciplinaListView.as_view(), name='disciplinas'),
]
