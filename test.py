import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

con = os.getenv("SENHA")

conexao = mysql.connector.connect(
    host = "MacBook-Air-de-Felipe-3.local",
    database = "teste",
    user = "lain",
    password = con
)

cursor = conexao.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS teste_mysql (valor TEXT)")

cursor.execute("INSERT INTO teste_mysql (valor) VALUES ('poderosa')")

conexao.commit()