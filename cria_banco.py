import sqlite3

connection = sqlite3.connect('banco.db')
cursor = connection.cursor()

cria_tabela = "CREATE TABLE IF NOT EXISTS agenda (agenda_id text PRIMARY KEY, nome text, numero text, email text, cidade text)"

cria_contato = "INSERT INTO agenda VALUES ('1', 'HENRIQUE', '2222', 'henrique@gmail.com', 'juazeiro do norte')"


cursor.execute(cria_tabela)
cursor.execute(cria_contato)
connection.commit()
connection.close()

#agenda_id, nome, numero, email, cidade