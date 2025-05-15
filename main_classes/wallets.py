from datetime import datetime

# To create and manage multiple wallets (max 5)

class Wallet:
    def __init__(self):
        self.wallets = []
        self.transactions = []

    def add_wallet (self, wallet_name,opening_balance):
        if len(self.wallets) >= 5:
            return ('The number of wallets is limited to five')
        self.wallets.append(wallet_name)
        self.wallets[wallet_name] = {"Initial balance": opening_balance}

        #Registers de opening balance as the first transaction in the wallet
        if opening_balance != 0.0:
            self.transactions.append({
                "wallet": wallet_name,
                "amount": opening_balance,
                "type": "Initial balance",
                "timestamp": datetime.now().isoformat()
            })
        return True

    def rename_wallet (self,old_name, new_name):
        if old_name in self.wallets:
            index = self.wallets.index(old_name)
            self.wallets[index] = new_name
            return True
        return False

    def delete_wallet_and_transactions (self, wallet_name, delete_transactions=False):
        self.wallets.remove(wallet_name)
        self.transactions = [t for t in self.transactions if t["wallet"] != wallet_name ]

    def delete_wallet_keep_transactions (self, wallet_name):
        self.wallets.remove(wallet_name)
        for t in self.transactions:
            if t["wallet"] == wallet_name:
                t["wallet"] = f"{wallet_name} [Deleted]"

    def adjust_balance(self,wallet_name,new_balance):
        current_balance = self.get_wallet_balance(wallet_name)    #To be created in the transactions classe, to update the balance with each transation
        difference = new_balance - current_balance

        if difference == 0:
            return

        self.transactions.append({
            "wallet": wallet_name,
            "amount": difference,
            "type": "Manual adjustment",
            "description": "Manual adjustment",
            "timestamp": datetime.now().isoformat()
        })

# Para gerir múltiplas carteiras