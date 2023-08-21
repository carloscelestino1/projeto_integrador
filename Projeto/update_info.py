import sqlite3

conn = sqlite3.connect('DatabaseProjeto.db')

cursor = conn.cursor()

def up_idade():
    id_pessoa = int(input('ID da pessoa: '))
    nova_idade = int(input('Nova idade: '))

    cursor.execute(f'UPDATE Info_Cadastrados SET Idade = {nova_idade} WHERE Id_Pessoa = {id_pessoa}')
    
    conn.commit()


def up_endereço():
    id_pessoa = int(input('ID da pessoa: '))
    novo_endereço = input('Novo endereço: ')

    cursor.execute(f'UPDATE Info_Cadastrados SET Endereço = {novo_endereço} WHERE Id_Pessoa = {id_pessoa}')
    
    conn.commit()


def up_tel():
    id_pessoa = int(input('ID da pessoa: '))
    novo_tel = input('Novo telefone: ')

    cursor.execute(f'UPDATE Info_Cadastrados SET Telefone = {novo_tel} WHERE Id_Pessoa = {id_pessoa}')
    
    conn.commit()


def up_nat():
    id_pessoa = int(input('ID da pessoa: '))
    nova_naturalidade = input('Nova naturalidade: ')

    cursor.execute(f'UPDATE Info_Cadastrados SET Naturalidade = {nova_naturalidade} WHERE Id_Pessoa = {id_pessoa}')
    
    conn.commit()


def up_esc():
    id_pessoa = int(input('ID da pessoa: '))
    nova_esc = input('Nova escolaridade: ')

    cursor.execute(f'UPDATE Info_Cadastrados SET Escolaridade = {nova_esc} WHERE Id_Pessoa = {id_pessoa}')
    
    conn.commit()


def up_renda():
    id_pessoa = int(input('ID da pessoa: '))
    nova_renda = float(input('Nova renda: '))

    cursor.execute(f'UPDATE Info_Cadastrados SET Renda = {nova_renda} WHERE Id_Pessoa = {id_pessoa}')
    
    conn.commit()


def up_ec():
    id_pessoa = int(input('ID da pessoa: '))
    novo_ec = input('Nova estado civil: ')

    cursor.execute(f'UPDATE Info_Cadastrados SET EC = {novo_ec} WHERE Id_Pessoa = {id_pessoa}')
    
    conn.commit()


def up_nis():
    id_pessoa = int(input('ID da pessoa: '))
    novo_nis = input('Nova NIS: ')

    cursor.execute(f'UPDATE Info_Cadastrados SET NIS = {novo_nis} WHERE Id_Pessoa = {id_pessoa}')
    
    conn.commit()
