# Generated by Django 3.0.6 on 2020-06-02 00:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0005_automovel_conjuge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='automovel',
            name='pessoa',
        ),
        migrations.RemoveField(
            model_name='conjuge',
            name='pessoa',
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('idade', models.IntegerField(default=0)),
                ('cpf', models.CharField(max_length=14, null=True)),
                ('automovel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.Automovel')),
                ('conjuge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.Conjuge')),
            ],
        ),
    ]
