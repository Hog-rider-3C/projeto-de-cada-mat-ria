import time
import random


class LojaMonolitica:
    def __init__(self):
        self.users = []
        self.products = []
        self.orders = []

    def add_user(self, user):
        self.users.append(user)

    def add_product(self, product):
        self.products.append(product)

    def process_payment(self):
        print("Processando pagamento...")
        time.sleep(1)  # simula lentidão

        if random.choice([True, False]):
            return True
        return False

    def place_order(self, user, product):
        if product not in self.products:
            return "Produto indisponível"

        if self.process_payment():
            self.orders.append((user, product))
            return "Pedido realizado com sucesso"
        else:
            return "Pagamento falhou - pedido cancelado"


def run():
    loja = LojaMonolitica()

    loja.add_user("Alice")
    loja.add_product("Laptop")

    print("\n=== MONOLITO ===")
    resultado = loja.place_order("Alice", "Laptop")
    print(resultado)

    return len(loja.orders)


if __name__ == "__main__":
    run()