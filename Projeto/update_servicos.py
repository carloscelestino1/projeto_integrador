import sqlite3

conn = sqlite3.connect('DatabaseProjeto.db')

def up_serviços():
    id_serviço = int(input('Digite o ID do serviço:' ))
    novo_serviço = input('Digite o novo serviço: ')

    conn.execute(f'UPDATE Serviços SET Serviços = "{novo_serviço}" WHERE Id_Serviço = {id_serviço}')

    conn.commit()

up_serviços()