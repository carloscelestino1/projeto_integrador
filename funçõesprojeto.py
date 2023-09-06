import sqlite3
import requests
import json
import re
from django.db import connection

conn = sqlite3.connect('DatabaseProjeto.db', check_same_thread= False) #Conexão com o banco
conn.row_factory = lambda cursor, row: row[0] #Retira os dados do banco das tuplas
cursor = conn.cursor()

def cadastro(name, dn, rg_, cpf_, idade_, end, tel, nat, esc, renda_, ec_, nis_): #Função de cadatros
    nome = name
    data_nascimento = dn
    rg = rg_
    cpf = cpf_

    rg_query = cursor.execute('SELECT RG from main_cadastrados')  # Ler todos RG que existem em cadastros
    rg_list = []
    for a in rg_query:
        rg_list.append(a)

    cpf_query = cursor.execute('SELECT CPF from main_cadastrados') # Ler todos CPF que exitem em cadastros
    cpf_list = []
    for i in cpf_query:
        cpf_list.append(i)

    if rg not in rg_list: # Se existir o rg no banco ele não cadastra 
        if cpf not in cpf_list: # Se existir o cpf no banco ele não cadastra 
            idade = idade_
            endereco = end
            telefone = tel
            naturalidade = nat
            escolaridade = esc
            renda = renda_
            ec = ec_
            nis = nis_

            nis_query = cursor.execute("SELECT NIS FROM main_cadastrados")
            nis_list = []
            for b in nis_query:
                nis_list.append(b)

            if nis not in nis_list: # Se existir o nis no banco ele não cadastra 
                    query_info = (f'''
                        INSERT INTO main_cadastrados(
                            Nome,
                            Data_Nascimento,
                            RG,
                            CPF,
                            Idade,
                            Endereço,
                            Telefone,
                            Naturalidade,
                            Escolaridade,
                            Renda,
                            EC,
                            NIS
                        )
                        VALUES(
                            '{nome}',
                            '{data_nascimento}',
                            '{rg}',
                            '{cpf}',
                            '{idade}',
                            '{endereco}',
                            '{telefone}',
                            '{naturalidade}',
                            '{escolaridade}',
                            '{renda}',
                            '{ec}',
                            '{nis}'
                            )
                    '''
                        )

                    cursor.execute(query_info)

            else: return False
        else: return False
    else: return False

    conn.commit()


def add_trabalho(trab): #Adicionar novo trabalho ao banco
    trabalho = trab

    trabalho_querry = cursor.execute("SELECT Serviços FROM main_servios")
    trab_list = []
    for i in trabalho_querry:
        trab_list.append(i)
    
    if trabalho not in trab_list: # Se o trabalho existir ele não adiciona ao banco

        query = f'''
            INSERT INTO main_servios (Serviços)
            VALUES ('{trabalho}')
        '''
        cursor.execute(query)

    else: return False

    conn.commit()


def designar_trabalho(name, id_serv, id): # Define um trabalho a uma pessoa
    nome = name
    query = cursor.execute(f"SELECT Nome FROM main_cadastrados")
    query_list = []
    for i in query:
        query_list.append(i)

    if nome in query_list: # Verifica se a pessoa se encontra no banco
        id_servico = id_serv
        id_pessoa = id

        conn.execute(f"INSERT INTO main_empregados(Id_Pessoa, Id_Serviço) VALUES ('{id_pessoa}', '{id_servico}')")

    else: return False
    conn.commit()

def consult_cnpj(cnpj): # Verfica se o cnpj é válido
    cnpj_= cnpj
    cnpj_ = re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ: ]', '', cnpj_)
    url = f"https://receitaws.com.br/v1/cnpj/{cnpj_}"
    querystring = {f"token":"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX", "cnpj":"06990590000123", "plugin":"RF"} # Determinar a quantidade de caracteres e a formatação que o sistema irá receber
    response = requests.request('GET', url, params=querystring)

    resp = json.loads(response.text)

    return(resp)


def save_infocnpj(cnpj, nome, local, tel, email): # Função de cadastro de Empresa no banco
    cnpj1 = cnpj
    name = nome
    end = local
    tele = tel
    contato = email

    query = (f'''INSERT INTO main_empresas (CNPJ, Nome, Endereço,
            Telefone, Email     
        ) VALUES ('{cnpj1}', '{name}', '{end}', '{tele}', '{contato}')''')

    cursor.execute(query)

    conn.commit()

def add_contato(nome1, email2, mensagem): # Função para entrar em contato com o Sistema, para sugestões ou reclamações
    nome = nome1
    email = email2
    msg = mensagem

    query = (f'''INSERT INTO main_contato(Nome, Email, Mensagem)
            VALUES ('{nome}', '{email}', '{msg}')
        ''')

    cursor.execute(query)

    conn.commit()

def tabela_servicos():
    with connection.cursor() as cursor:
        query = '''
        SELECT main_cadastrados.nome as "Nome",
               main_cadastrados.telefone as "Telefone",
               main_servios.serviços as "Serviço",
               main_foto_cadastrados.foto as "Foto"
        FROM main_empregados
        INNER JOIN main_cadastrados ON main_cadastrados.id_pessoa = main_empregados.id_pessoa
        INNER JOIN main_servios ON main_servios.id_serviço = main_empregados.id_serviço
        INNER JOIN main_foto_cadastrados ON main_foto_cadastrados.id = main_cadastrados.id_pessoa
        '''
        cursor.execute(query)
        results = cursor.fetchall()
        return results