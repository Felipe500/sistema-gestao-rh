# Generated by Django 3.2.9 on 2022-02-01 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0002_alter_funcionario_nome'),
        ('documentos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='funcionario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='funcionario.funcionario'),
        ),
    ]
