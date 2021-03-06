from django.db import models

from principal.models import AnoEscolar


class Turma(models.Model):

	TURMA_NOME_CHOICES = (
		('A', 'A'),
		('B', 'B'),
		('C', 'C'),
		('D', 'D')
	)

	turma_id = models.AutoField(
		primary_key=True
	)
	turma_ano_escolar = models.ForeignKey(
		AnoEscolar,
		verbose_name='Ano Escolar',
		on_delete=models.DO_NOTHING,
		related_name='turmaanoescolar'
	)
	turma_nome = models.CharField(
		'Nome',
		max_length=1,
		choices=TURMA_NOME_CHOICES,
		default='A'
	)

	def turma_codigo_id(self):
		"""
		Return custom unique identification
		"""
		return 'turma-' + str(self.turma_id)

	def turma_nome_completo(self):
		"""
		Return complete 'Turma' name
		"""
		ano_escolar = self.turma_ano_escolar
		turma_nome_min = ano_escolar.get_ano_escolar_nome_display()
		turma_ano = ano_escolar.ano_escolar_etapa.etapa_basica_ano

		return f'{turma_nome_min} {self.turma_nome} {turma_ano}'

	def turma_ano_letivo(self):
		"""
		Return Year of 'Turma'
		"""
		ano_escolar = self.turma_ano_escolar
		turma_ano = ano_escolar.ano_escolar_etapa.etapa_basica_ano

		return turma_ano

	class Meta:
		verbose_name = 'Turma'
		verbose_name_plural = 'Turmas'
		constraints = [
			models.UniqueConstraint(
				fields=['turma_ano_escolar', 'turma_nome'],
				name='unica_turma_ano'
			)
		]
		ordering = ['turma_ano_escolar', 'turma_nome']

	def __str__(self):
		return self.turma_nome_completo()

