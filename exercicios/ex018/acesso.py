import sqlite3


busca = input("Quem você está procurando? ").strip()

try:
    with sqlite3.connect("meubanco.db") as banco:
        banco.row_factory = sqlite3.Row
        cur = banco.cursor()
        cur.execute("SELECT * FROM amigos WHERE nome like ?", (f"%{busca}%",))
        # lista = cur.fetchall()
        # print(lista)

        total = 0

        for total, amigo in enumerate(cur, start=1):
            print(f"{amigo['nome']} nasceu em {amigo['nascimento']}")

        print(f"Ao todo encontrei {total} amigo(s) com '{busca}'")

except sqlite3.Error as erro:
    print(f"Falha no banco: {erro}")

except Exception as erro:
    print(f"Algo deu errado: {erro}!")

print("ACABOU!")
