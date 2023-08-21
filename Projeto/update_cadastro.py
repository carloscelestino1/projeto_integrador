import sqlite3
conn = sqlite3.connect('DatabaseProjeto.db')
cursor = conn.cursor()

def up_nome():
    id_pessoa = int(input('Digite o ID da pessoa: '))
    novo_nome = input('Atualize o nome: ')
    conn.execute(f'UPDATE Cadastros SET Nome = "{novo_nome}" WHERE Id_Pessoa ="{id_pessoa}" ')

    conn.commit()

def up_dn():
    id_pessoa = int(input('Digite o ID da pessoa: '))
    nova_data_nascimento = input('Atualize a data de nascimento: ')
    conn.execute(f'UPDATE Cadastros SET Data_nascimento = "{nova_data_nascimento}" WHERE Data_nascimento ="{id_pessoa}" ')

    conn.commit()

def up_rg():
    id_pessoa = int(input('Digite o ID da pessoa: '))
    novo_rg = input('Atualize o RG: ')
    conn.execute(f'UPDATE Cadastros SET RG = "{novo_rg}" WHERE Id_Pessoa ="{id_pessoa}" ')

    conn.commit()

def up_cpf():
    id_pessoa = int(input('Digite o ID da pessoa: '))
    novo_cpf = input('Atualize o CPF: ')
    conn.execute(f'UPDATE Cadastros SET CPF = "{novo_cpf}" WHERE Id_Pessoa ="{id_pessoa}" ')

    conn.commit()