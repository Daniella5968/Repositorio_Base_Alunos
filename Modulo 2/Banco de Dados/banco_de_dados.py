import sqlite3

try:
    con = sqlite3.connect("meu_banco.db")
    cur = con.cursor()
    # cur.execute("create table pessoa(id,nome,idade,cpf)")
    # cur.execute("INSERT INTO pessoa VALUES(1, 'Daniella', 27, 'xxx.xxx.xxx-xx')") 
    # cur.execute("INSERT INTO pessoa VALUES(6, 'Sarah', 15, '409-879-989.55')")
    # cur.execute("INSERT INTO pessoa VALUES(8, 'Miguel', 30, '598-974-934.00')")
    # cur.execute("INSERT INTO pessoa VALUES(1, 'Kauan', 50, '709-456-345.88')")
    # cur.execute("INSERT INTO pessoa VALUES(1, 'Mariana', 20, '209-921-123.34')")
    # cur.execute("INSERT INTO pessoa VALUES(9, 'Pedro', 19, '608-908-999.55' )")
    # cur.execute("INSERT INTO pessoa VALUES(4, 'Maicon', 25, '534-796-435.32' )")
    # cur.execute("INSERT INTO pessoa VALUES(3, 'Joaquin', 13, '543-523-654.09')")
    # cur.execute("INSERT INTO pessoa VALUES(67, 'Maria', 36, '890-875-454.11')")
    # cur.execute("INSERT INTO pessoa VALUES(3,'Clara', 50, '340-987-333.88')")
    # cur.execute("INSERT INTO pessoa VALUES(5, 'Juan', 18, '687-345-789.99' )")
    
    con.commit()
    
except ConnectionRefusedError as c:
    print('Erro de conexão com o banco.')
