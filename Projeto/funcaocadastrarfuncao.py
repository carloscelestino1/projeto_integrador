import sqlite3

conn = sqlite3.connect('DatabaseProjeto.db')

cursor = conn.cursor()

def designar_trabalho():

    nome = input('digite o seu nome: ')

    cursor = conn.execute(f'SELECT Id_Pessoa FROM Cadastros WHERE Nome = "{nome}"')

    for i in cursor:
        print(f'O ID de {nome} é', i)

    query = cursor.execute(f'SELECT * FROM Serviços')
    for i in query:
        print(i)

    id_servico = int(input('insira o id do serviço: '))
    id_pessoa = int(input('insira o id do empregado: '))

    conn.execute(f"INSERT INTO Empregados(Id_Pessoa, Id_Serviço) VALUES ('{id_pessoa}', '{id_servico}')")

    conn.commit()

designar_trabalho()



