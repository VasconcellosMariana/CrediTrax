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
        signal = "+" if self.type == "income" else "-"
        return f"{self.date} | {self.category} | {signal}{self.value:.2f} | {self.description}"


class CategoryManager:
    def __init__(self, conn):
        self.conn = conn

    def list(self, type):
        cursor = self.conn.cursor()
        cursor.execute("SELECT name FROM categories WHERE type=? ORDER BY name", (type,))
        return [row[0] for row in cursor.fetchall()]

    def add(self, name, type):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO categories (name, type, origin)
            VALUES (?, ?, 'custom')
        """, (name, type))
        self.conn.commit()


def can_add_transaction(type, value, category, wallet_id):
    return all([
        type in ['income', 'expense'],
        value > 0,
        wallet_id is not None,
        category not in [None, '']
    ])


# Compra e venda de ações


# Atualização do preço das ações e estimativa de património líquido global




# Agendamento de transações