import time


class OnlineStore:
    def __init__(self):
        self.products = ["Laptop"]
        self.orders = []

    def place_order(self, user, product):
        print(f"Monólito -> processando pedido de {user}...")

        time.sleep(0.08)  # mais lento

        if product in self.products:
            self.orders.append((user, product))
            return True

        return False