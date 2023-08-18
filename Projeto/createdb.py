import sqlite3

conn = sqlite3.connect('DatabaseProjeto.db')
cursor = conn.cursor()

cursor.execute('''
        CREATE TABLE Cadastros(
            Id_Pessoa INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome TEXT,
            Data_Nascimento DATE,
            RG TEXT,
            CPF TEXT
        )
''')

cursor.execute('''
        CREATE TABLE Info_Cadastrados(
            Id_Info INTEGER PRIMARY KEY AUTOINCREMENT,
            Id_Pessoa INT,
            Idade INT,
            Endereço TEXT,
            Telefone TEXT,
            Naturalidade TEXT,
            Escolaridade TEXT,
            Renda REAL,
            EC TEXT,
            NIS TEXT,
            FOREIGN KEY (Id_Pessoa) REFERENCES Cadastros (Id_Pessoa)
        )
''')

cursor.execute('''
        CREATE TABLE Serviços(
            Id_Serviço INTEGER PRIMARY KEY AUTOINCREMENT,
            Serviços TEXT
        )
''')

cursor.execute('''
        CREATE TABLE Empregados(
            Id_Empregados INTEGER PRIMARY KEY AUTOINCREMENT,
            Id_Pessoa INT,
            Id_Serviço INT,
            FOREIGN KEY (Id_Pessoa) REFERENCES Cadastros (Id_Pessoa),
            FOREIGN KEY (Id_Serviço) REFERENCES Serviços (Id_Serviço)
        )
''')

conn.commit()
cursor.close()