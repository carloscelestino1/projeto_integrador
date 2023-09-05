from django.db import models
from django.contrib.auth import get_user_model




class Cadastrados(models.Model):
    id_pessoa = models.AutoField(db_column='Id_Pessoa', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    nome = models.TextField(db_column='Nome', blank=True, null=True)  # Field name made lowercase.
    data_nascimento = models.TextField(db_column='Data_Nascimento', blank=True, null=True)  # Field name made lowercase.
    rg = models.TextField(db_column='RG', blank=True, null=True)  # Field name made lowercase.
    cpf = models.TextField(db_column='CPF', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    idade = models.TextField(db_column='Idade', blank=True, null=True)
    endereço = models.TextField(db_column='Endereço', blank=True, null=True)  # Field name made lowercase.
    telefone = models.TextField(db_column='Telefone', blank=True, null=True)  # Field name made lowercase.
    naturalidade = models.TextField(db_column='Naturalidade', blank=True, null=True)  # Field name made lowercase.
    escolaridade = models.TextField(db_column='Escolaridade', blank=True, null=True)  # Field name made lowercase.
    renda = models.FloatField(db_column='Renda', blank=True, null=True)  # Field name made lowercase.
    ec = models.TextField(db_column='EC', blank=True, null=True)  # Field name made lowercase.
    nis = models.TextField(db_column='NIS', blank=True, null=True)  # Field name made lowercase.




class Contato(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    nome = models.TextField(db_column='Nome', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase.
    mensagem = models.TextField(db_column='Mensagem', blank=True, null=True)  # Field name made lowercase.




class Empregados(models.Model):
    id_empregados = models.AutoField(db_column='Id_Empregados', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    id_pessoa = models.ForeignKey(Cadastrados, models.DO_NOTHING, db_column='Id_Pessoa', blank=True, null=True)  # Field name made lowercase.
    id_serviço = models.ForeignKey('Servios', models.DO_NOTHING, db_column='Id_Serviço', blank=True, null=True)  # Field name made lowercase.




class Empresas(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    cnpj = models.TextField(db_column='CNPJ', blank=True, null=True)  # Field name made lowercase.
    nome = models.TextField(db_column='Nome', blank=True, null=True)  # Field name made lowercase.
    endereço = models.TextField(db_column='Endereço', blank=True, null=True)  # Field name made lowercase.
    telefone = models.TextField(db_column='Telefone', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase.





class Foto_Cadastrados(models.Model):
    id_pessoa = models.ForeignKey(Cadastrados, models.DO_NOTHING, db_column='Id_Pessoa', blank=True, null=True)
    foto = models.ImageField(upload_to='', db_column='Foto', blank=True, null=True)
    def __str__(self):
        return str(self.id_pessoa)



class Servios(models.Model):
    id_serviço = models.AutoField(db_column='Id_Serviço', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    serviços = models.TextField(db_column='Serviços', blank=True, null=True)  # Field name made lowercase.