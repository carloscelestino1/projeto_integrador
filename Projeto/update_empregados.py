import sqlite3

conn = sqlite3.connect('DatabaseProjeto.db')

def up_serviço():
    id_pessoa = int(input("Digite o ID da pessoa:"))
    id_servicos = int(input('Digite o ID do serviço:'))

    conn.execute(f'UPDATE Empregados SET Id_Serviço = {id_servicos} WHERE Id_Pessoa = {id_pessoa}' )

    conn.commit()

up_serviço()