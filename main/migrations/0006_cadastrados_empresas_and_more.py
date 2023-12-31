# Generated by Django 4.2.4 on 2023-08-31 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_mainempresas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastrados',
            fields=[
                ('id_pessoa', models.AutoField(db_column='Id_Pessoa', primary_key=True, serialize=False)),
                ('nome', models.TextField(blank=True, db_column='Nome', null=True)),
                ('data_nascimento', models.TextField(blank=True, db_column='Data_Nascimento', null=True)),
                ('rg', models.TextField(blank=True, db_column='RG', null=True)),
                ('cpf', models.TextField(blank=True, db_column='CPF', null=True)),
                ('idade', models.TextField(blank=True, db_column='Idade', null=True)),
                ('endereço', models.TextField(blank=True, db_column='Endereço', null=True)),
                ('telefone', models.TextField(blank=True, db_column='Telefone', null=True)),
                ('naturalidade', models.TextField(blank=True, db_column='Naturalidade', null=True)),
                ('escolaridade', models.TextField(blank=True, db_column='Escolaridade', null=True)),
                ('renda', models.FloatField(blank=True, db_column='Renda', null=True)),
                ('ec', models.TextField(blank=True, db_column='EC', null=True)),
                ('nis', models.TextField(blank=True, db_column='NIS', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empresas',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('cnpj', models.TextField(blank=True, db_column='CNPJ', null=True)),
                ('nome', models.TextField(blank=True, db_column='Nome', null=True)),
                ('endereço', models.TextField(blank=True, db_column='Endereço', null=True)),
                ('telefone', models.TextField(blank=True, db_column='Telefone', null=True)),
                ('email', models.TextField(blank=True, db_column='Email', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='infocadastrados',
            name='id_pessoa',
        ),
        migrations.DeleteModel(
            name='MainEmpresas',
        ),
        migrations.AlterField(
            model_name='contato',
            name='email',
            field=models.TextField(blank=True, db_column='Email', null=True),
        ),
        migrations.AlterField(
            model_name='contato',
            name='id',
            field=models.AutoField(db_column='Id', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='contato',
            name='nome',
            field=models.TextField(blank=True, db_column='Nome', null=True),
        ),
        migrations.DeleteModel(
            name='InfoCadastrados',
        ),
        migrations.AlterField(
            model_name='empregados',
            name='id_pessoa',
            field=models.ForeignKey(blank=True, db_column='Id_Pessoa', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.cadastrados'),
        ),
        migrations.AlterField(
            model_name='foto_cadastrados',
            name='id_pessoa',
            field=models.ForeignKey(blank=True, db_column='Id_Pessoa', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.cadastrados'),
        ),
        migrations.DeleteModel(
            name='Cadastros',
        ),
    ]
