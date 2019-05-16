# Generated by Django 2.1.7 on 2019-03-24 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lanc_notas', '0002_auto_20190316_1223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno_Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alunos', models.ManyToManyField(to='lanc_notas.Aluno')),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lanc_notas.Turma')),
            ],
        ),
    ]
