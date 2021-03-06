# Generated by Django 3.2.9 on 2022-02-01 20:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0002_alter_departamento_nome'),
        ('empresa', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('funcionario', '0002_alter_funcionario_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='departamentos',
            field=models.ManyToManyField(to='departamento.Departamento'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='empresa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='empresa.empresa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='funcionario',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='auth.user'),
            preserve_default=False,
        ),
    ]
