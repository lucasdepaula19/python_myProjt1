# Generated by Django 3.0.6 on 2020-05-24 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_endereco_bairro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='data_nascimento',
        ),
    ]