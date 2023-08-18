import sqlite3

conn = sqlite3.connect('DatabaseProjeto.db')
conn.row_factory = lambda cursor, row: row[0]
cursor = conn.cursor()

def add_trabalho():
    trabalho = input('Digite o trabalho que deseja adicionar: ')

    trabalho_querry = cursor.execute("SELECT Serviços FROM Serviços")
    trab_list = []
    for i in trabalho_querry:
        trab_list.append(i)
    print(trab_list)
    
    if trabalho not in trab_list:

        query = f'''
            INSERT INTO Serviços (Serviços)
            VALUES ('{trabalho}')
        '''
        cursor.execute(query)

    else: print('Trabalho já cadastrado')

    conn.commit()

add_trabalho()