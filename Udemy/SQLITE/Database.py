import sqlite3

#Criando uma conexão passando o nome do arquivo
conn = sqlite3.connect('myDatabase.db')

#Obtendo um cursor
c = conn.cursor()

#Função para criar a tabela
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS cars(name TEXT, year INTEGER, price REAL)')

#Função para inserir um registro
def insert_entry(name, year, price):
    c.execute('INSERT INTO cars (name, year, price) VALUES (?, ?, ?)', \
    (name, year, price))
    conn.commit()

#Função para mostrar todos os registros
def show_all():
    print('\nExibindo todos os registros:\n')
    c.execute('SELECT * FROM cars')
    rows = c.fetchall()
    
    for row in rows:
        print(row)

#Função para mostrar um único registro pelo nome
def show_entry(name):
    print('\nExibindo o registro %s\n' % name)
    c.execute('SELECT name, year, price FROM cars WHERE name=:name', {'name': name})
    row = c.fetchone()
    if row:
        print(row)

#Função para atualizar o nome dos registros
def update_name(old_name, new_name):
    c.execute('UPDATE cars SET name=? WHERE name=?', \
    (new_name, old_name))

#Cria tabela
create_table()

#Insere os registros
insert_entry('Camaro', 2015, 200000)
insert_entry('Jaguar', 2016, 600000)
insert_entry('Azera', 2017, 120000)

#Exibe todos os registros
show_all()

#Exibe um único registro
show_entry('Azera')

#Atualiza um registro
update_name('Camaro', 'Fusca')
show_all()

#Fecha o cursor e a conexão
c.close()
conn.close()