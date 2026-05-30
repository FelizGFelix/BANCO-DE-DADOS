import sqlite3

nome_user = input("Digite o seu nome usuário: ")
email_user = input("Digite o seu email: ")
senha_user = input("Digite a sua senha: ")

print("Perfil criado com sucesso!")

banco = sqlite3.connect("perfil.db")

cursor = banco.cursor()

cursor.execute("CREATE TABLE informacoes(nome TEXT, email TEXT, senha TEXT)")

cursor.execute("INSERT INTO informacoes VALUES('"+nome_user+"', '"+email_user+"', '"+senha_user+"')")

banco.commit()
banco.close()