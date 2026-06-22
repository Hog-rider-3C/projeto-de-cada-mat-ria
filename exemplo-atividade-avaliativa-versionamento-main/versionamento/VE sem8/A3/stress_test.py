import time


def run_test(system, total):
    inicio = time.time()
    sucesso = 0

    for i in range(1, total + 1):
        user = f"user{i}"

        if system.place_order(user, "Laptop"):
            sucesso += 1

    tempo = time.time() - inicio

    return sucesso, tempo