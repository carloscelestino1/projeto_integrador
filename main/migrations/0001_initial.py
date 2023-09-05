# Generated by Django 4.2.4 on 2023-08-25 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastros',
            fields=[
                ('id_pessoa', models.AutoField(db_column='Id_Pessoa', primary_key=True, serialize=False)),
                ('nome', models.TextField(blank=True, db_column='Nome', null=True)),
                ('data_nascimento', models.DateField(blank=True, db_column='Data_Nascimento', null=True)),
                ('rg', models.TextField(blank=True, db_column='RG', null=True)),
                ('cpf', models.TextField(blank=True, db_column='CPF', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Servios',
            fields=[
                ('id_serviço', models.AutoField(db_column='Id_Serviço', primary_key=True, serialize=False)),
                ('serviços', models.TextField(blank=True, db_column='Serviços', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InfoCadastrados',
            fields=[
                ('id_info', models.AutoField(db_column='Id_Info', primary_key=True, serialize=False)),
                ('idade', models.IntegerField(blank=True, db_column='Idade', null=True)),
                ('endereço', models.TextField(blank=True, db_column='Endereço', null=True)),
                ('telefone', models.TextField(blank=True, db_column='Telefone', null=True)),
                ('naturalidade', models.TextField(blank=True, db_column='Naturalidade', null=True)),
                ('escolaridade', models.TextField(blank=True, db_column='Escolaridade', null=True)),
                ('renda', models.FloatField(blank=True, db_column='Renda', null=True)),
                ('ec', models.TextField(blank=True, db_column='EC', null=True)),
                ('nis', models.TextField(blank=True, db_column='NIS', null=True)),
                ('id_pessoa', models.ForeignKey(blank=True, db_column='Id_Pessoa', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.cadastros')),
            ],
        ),
        migrations.CreateModel(
            name='Empregados',
            fields=[
                ('id_empregados', models.AutoField(db_column='Id_Empregados', primary_key=True, serialize=False)),
                ('id_pessoa', models.ForeignKey(blank=True, db_column='Id_Pessoa', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.cadastros')),
                ('id_serviço', models.ForeignKey(blank=True, db_column='Id_Serviço', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.servios')),
            ],
        ),
    ]
