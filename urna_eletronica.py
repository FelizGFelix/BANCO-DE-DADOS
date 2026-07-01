import sqlite3
import os 

def limpar():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

num_disp = [12, 27, 30, 22, 80, 13, 14, 15, 21, 44, 16]

while True:
    banco = sqlite3.connect("votos.db")
    cursor = banco.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS votos_registrados(voto INT)")

    print("Escolhe o número do candidato:\n")
    voto_escolhido = int(input("-> "))

    if voto_escolhido not in num_disp:
        print("Digite um número válido")

    else:
        limpar()
        print("Voto registrado!")

        cursor.execute("INSERT INTO votos_registrados VALUES (?)", (voto_escolhido,))

        banco.commit()
        banco.close()
        break