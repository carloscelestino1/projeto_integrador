import sqlite3

conn = sqlite3.connect('DatabaseProjeto.db')
conn.row_factory = lambda cursor, row: row[0]
cursor = conn.cursor()

def cadastro():
    nome = input('Digite o nome completo: ')
    data_nascimento = input('Digite a data de nascimento: ')
    rg = input('Digite o RG: ')
    cpf = input('Digite o CPF: ')

    rg_query = cursor.execute('SELECT RG from Cadastros')
    rg_list = []
    for a in rg_query:
        rg_list.append(a)

    cpf_query = cursor.execute('SELECT CPF from Cadastros')
    cpf_list = []
    for i in cpf_query:
        cpf_list.append(i)

    if rg not in rg_list:
        if cpf not in cpf_list:
            idade = input('Digite a idade: ')
            endereco = input('Digite o endereço: ')
            telefone = input('Digite o telefone: ')
            naturalidade = input('Digite a Naturalidade: ')
            escolaridade = input('Digite a escolaridade: ')
            renda = input('Digite a renda: ')
            ec = input('Digite o estado civil: ')
            nis = input('Digite o NIS: ')

            nis_query = cursor.execute("SELECT NIS FROM Info_Cadastrados")
            nis_list = []
            for b in nis_query:
                nis_list.append(b)

            if nis not in nis_list:
                query = '''
                    INSERT INTO Cadastros
                    (Nome, Data_Nascimento, RG, CPF)
                    VALUES (?, ?, ?, ?)
                    '''

                data_insert = (
                    nome,
                    data_nascimento,
                    rg,
                    cpf
                )

                cursor.execute(query, data_insert)

                id_pessoa_query = cursor.execute(f"\
                    SELECT Id_Pessoa FROM Cadastros\
                    WHERE CPF = '{cpf}' ")
                result = id_pessoa_query.fetchone()

                if result:
                    query_info = '''
                        INSERT INTO Info_Cadastrados(
                            Id_Pessoa,
                            Idade,
                            Endereço,
                            Telefone,
                            Naturalidade,
                            Escolaridade,
                            Renda,
                            EC,
                            NIS
                        )
                        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
                    '''

                    data_insert_info = (result,
                            idade,
                            endereco,
                            telefone,
                            naturalidade,
                            escolaridade,
                            renda,
                            ec,
                            nis)

                    cursor.execute(query_info, data_insert_info)

            else: print('NIS já cadastrado')
        else: print('CPF já cadastrado')   
    else: print('RG já cadastrado')
    
    conn.commit()

cadastro()