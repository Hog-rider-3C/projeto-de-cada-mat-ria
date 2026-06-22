import time


class ProductService:
    def __init__(self):
        self.products = ["Laptop"]

    def check_product(self, product):
        print("ProductService -> validando produto...")
        time.sleep(0.02)

        return product in self.products


class OrderService:
    def __init__(self):
        self.orders = []

    def place_order(self, user, product):
        print(f"OrderService -> registrando pedido de {user}...")
        time.sleep(0.02)

        self.orders.append((user, product))
        return True


class OnlineStoreMicro:
    def __init__(self):
        self.product_service = ProductService()
        self.order_service = OrderService()

    def place_order(self, user, product):
        if self.product_service.check_product(product):
            return self.order_service.place_order(user, product)

        return False