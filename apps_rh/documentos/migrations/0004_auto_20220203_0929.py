# Generated by Django 3.2.9 on 2022-02-03 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0003_alter_documento_funcionario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documento',
            old_name='funcionario',
            new_name='pertence',
        ),
        migrations.AddField(
            model_name='documento',
            name='arquivo',
            field=models.FileField(default=1, upload_to='documentos'),
            preserve_default=False,
        ),
    ]