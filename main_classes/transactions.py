from datetime import datetime

# Inserir um movimento

from datetime import datetime

class Movimento:

    def __init__(self, tipo, valor, categoria, descricao='', data=None, wallet_id=None, id=None):
        self.tipo = tipo
        self.valor = valor
        self.categoria = categoria
        self.descricao = descricao
        self.data = data if data else datetime.now().strftime("%Y-%m-%d %H:%M")
        self.wallet_id = wallet_id
        self.id = id

    def salvar_bd(self, conn):
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO transactions (valor, tipo, categoria, data, descricao, carteira_id)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (self.valor, self.tipo, self.categoria, self.data, self.descricao, self.wallet_id))
        conn.commit()
        self.id = cursor.lastrowid

    def __repr__(self):
        sinal = "+" if self.tipo == "receita" else "-"
        return f"{self.data} | {self.categoria} | {sinal}{self.valor:.2f} | {self.descricao}"


# Compra e venda de ações


# Atualização do preço das ações e estimativa de património líquido global




# Agendamento de transações