import sqlite3
from datetime import datetime, date


def tratar_nascimento(valor):
    if valor is None or not str(valor).strip():
        return "Data não informada", None

    try:
        nascimento = datetime.strptime(str(valor).strip(), "%Y-%m-%d").date()

    except ValueError:
        return "Data inválida", None

    hoje = date.today()

    if nascimento > hoje:
        return "Data no futuro", None

    data_formatada = nascimento.strftime("%d/%m/%Y")
    idade = hoje.year - nascimento.year

    if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
        idade -= 1

    return data_formatada, idade


busca = input("Quem você está procurando? ").strip()

try:
    with sqlite3.connect("meubanco.db") as banco:
        banco.row_factory = sqlite3.Row
        cur = banco.cursor()

        cur.execute("SELECT * FROM amigos WHERE nome LIKE ?", (f"%{busca}%",))

        total = 0

        for total, amigo in enumerate(cur, start=1):
            data_formatada, idade = tratar_nascimento(amigo["nascimento"])

            if data_formatada is None:
                mensagem = f"O cadastro de {amigo['nome']} não possui uma data de nascimento válida!"

            else:
                mensagem = f"{amigo['nome']} nasceu em {data_formatada}"

            if idade  is not None:
                mensagem += f" e tem {idade} anos!"

            print(mensagem)

        if total == 0:
            print(F"Não foi possível localizar '{busca}'")

        elif total == 1:
            print(f"Encontrei apenas um amigo com {busca}")

        else:
            print(f"Ao todo encontrei {total} amigo(s) com '{busca}'")

except sqlite3.Error as erro:
    print(f"Falha no banco: {erro}")

except Exception as erro:
    print(f"Algo deu errado: {erro}!")

print("ACABOU!")
