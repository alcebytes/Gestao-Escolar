# Generated by Django 3.1.3 on 2020-12-18 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0002_auto_20201218_1833'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aluno',
            options={'ordering': ['aluno_nome'], 'verbose_name': 'Aluno', 'verbose_name_plural': 'Alunos'},
        ),
    ]
