import os
import sqlite3
import os
import pandas as pd

def limpar():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

banco = sqlite3.connect("sociedade_mine.db")
cursor = banco.cursor()

class Cadastro_vila():
    def __init__(self):
        self.nome_jogador = ""
        self.funcao = ""
        self.cargo = ""

    def cadastro(self):
        cursor.execute("CREATE TABLE IF NOT EXISTS cadastro_vila ('codigo' INTEGER PRIMARY KEY AUTOINCREMENT,'nome' TEXT,'funcao' TEXT,'cargo' TEXT)")

        self.nome_jogador = input("Digite o nome do jogador: ")
        self.funcao = input("Digite sua função: ")
        self.cargo = input("Digite o cargo: ")

        cursor.execute("INSERT INTO cadastro_vila (nome, funcao, cargo) VALUES (?, ?, ?)", (self.nome_jogador, self.funcao, self.cargo, ))
        banco.commit()
        limpar()

    def excluir(self):
        index_jogador = int(input("Digite o index do jogador a ser deletado: "))
        cursor.execute("DELETE FROM cadastro_vila WHERE codigo = (?)", (index_jogador,))
        banco.commit()
        limpar()

    def mostrar_membros(self):
        comando = "SELECT * FROM cadastro_vila"
        df = pd.read_sql(comando, banco)

        pd.set_option('display.max_columns', None)
        print(df)

    def atualizar(self):
        index_jogador = int(input("Digite o index do jogador a ser alterado: "))
        
        self.nome_jogador = input("Digite o novo nome do jogador: ")
        self.funcao = input("Digite a nova função: ")
        self.cargo = input("Digite o novo cargo: ")

        cursor.execute("UPDATE cadastro_vila SET nome = ?, funcao = ?, cargo = ? WHERE codigo = ?", (self.nome_jogador, self.funcao, self.cargo, index_jogador, ))
        banco.commit()
        limpar()

iniciar = Cadastro_vila()

def main():
    resposta = 0

    while True:
        resposta = int(input("1- Fazer Cadastro\n2- Excluir Cadastro\n3- Mostrar Cadastros\n4- Atualizar Cadastro\n->"))

        if resposta == 1:
            limpar()
            iniciar.cadastro()
        
        elif resposta == 2:
            limpar()
            iniciar.excluir()

        elif resposta == 3:
            limpar()
            iniciar.mostrar_membros()

        elif resposta == 4:
            limpar()
            iniciar.atualizar()

if __name__ == "__main__":
    main()