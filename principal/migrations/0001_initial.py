# Generated by Django 3.1.3 on 2021-02-27 16:26

import base.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnoLetivo',
            fields=[
                ('ano_letivo_id', models.AutoField(primary_key=True, serialize=False)),
                ('ano_letivo_nome', models.CharField(max_length=4, unique=True, validators=[base.validators.validate_digits, base.validators.validate_ano_letivo], verbose_name='Ano Letivo')),
            ],
            options={
                'verbose_name': 'Ano Letivo',
                'verbose_name_plural': 'Anos Letivos',
                'ordering': ['-ano_letivo_nome'],
            },
        ),
        migrations.CreateModel(
            name='EtapaBasica',
            fields=[
                ('etapa_basica_id', models.AutoField(primary_key=True, serialize=False)),
                ('etapa_basica_nome', models.CharField(choices=[('IN', 'Infantil'), ('F1', 'Fundamental I'), ('F2', 'Fundamental II'), ('EM', 'Ensino Médio')], max_length=2, verbose_name='Etapa de Educação')),
                ('etapa_basica_ano', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='principal.anoletivo', verbose_name='Ano Letivo')),
            ],
            options={
                'verbose_name': 'Etapa Educação Básica',
                'verbose_name_plural': 'Etapas Educação Básica',
                'ordering': ['etapa_basica_ano', 'etapa_basica_nome'],
            },
        ),
        migrations.CreateModel(
            name='AnoEscolar',
            fields=[
                ('ano_escolar_id', models.AutoField(primary_key=True, serialize=False)),
                ('ano_escolar_nome', models.CharField(choices=[('CR', 'Creche'), ('G1', 'Maternal I'), ('G2', 'Maternal II'), ('G3', 'Maternal III'), ('G4', 'Jardim I'), ('G5', 'Jardim II'), ('1A', '1º Ano'), ('2A', '2º Ano'), ('3A', '3º Ano'), ('4A', '4º Ano'), ('5A', '5º Ano'), ('6A', '6º Ano'), ('7A', '7º Ano'), ('8A', '8º Ano'), ('9A', '9º Ano')], max_length=2, verbose_name='Ano escolar')),
                ('ano_escolar_etapa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.etapabasica', verbose_name='Etapa')),
            ],
            options={
                'verbose_name': 'Ano Escolar',
                'verbose_name_plural': 'Anos Escolares',
                'ordering': ['ano_escolar_etapa', 'ano_escolar_nome'],
            },
        ),
        migrations.AddConstraint(
            model_name='etapabasica',
            constraint=models.UniqueConstraint(fields=('etapa_basica_nome', 'etapa_basica_ano'), name='unica_etapa_no_ano'),
        ),
        migrations.AddConstraint(
            model_name='anoescolar',
            constraint=models.UniqueConstraint(fields=('ano_escolar_nome', 'ano_escolar_etapa'), name='unico_ano_escolar_na_etapa'),
        ),
    ]
