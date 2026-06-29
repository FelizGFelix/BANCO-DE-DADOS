import sqlite3

banco = sqlite3.connect("perfil_twitter.db")
cursor = banco.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS perfil2(usuario TEXT, senha TEXT, email TEXT)")

print("Crie a sua conta:")
nome_usuario = input("Digite o seu nome de úsuario: ")
senha_usuario = input("Digite a senha do seu perfil: ")
email_usuario = input("Digite o email da conta: ")

print(f"Conta criada com sucesso! seja bem vindo {nome_usuario}!")

cursor.execute("INSERT INTO perfil2 VALUES('"+nome_usuario+"', '"+senha_usuario+"', '"+email_usuario+"')")

banco.commit()
banco.close()

banco2 = sqlite3.connect("posts.db")
cursor2 = banco2.cursor()

cursor2.execute("CREATE TABLE IF NOT EXISTS posts(postagens TEXT)")

while True:
    post = input("Escreva o seu post:\n")

    cursor2.execute("INSERT INTO posts VALUES('"+post+"')")

    cursor2.execute("SELECT * FROM posts")

    dados = cursor2.fetchall

    print("--------------------------------------")

    print(dados)

    banco2.commit()
    banco2.close()