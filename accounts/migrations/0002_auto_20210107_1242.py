# Generated by Django 3.1.3 on 2021-01-07 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='identifier',
            field=models.CharField(max_length=30, unique=True, verbose_name='Usuário'),
        ),
    ]