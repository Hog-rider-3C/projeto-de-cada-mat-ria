import time

import monolitico as monolitico
import microsservicos as microsservicos


print("\n==============================")
print("COMPARANDO ARQUITETURAS")
print("==============================")


inicio = time.time()
pedidos_monolito = monolitico.run()
tempo_monolito = time.time() - inicio


inicio = time.time()
pedidos_micro = microsservicos.run()
tempo_micro = time.time() - inicio


print("\n===== RESULTADO =====")
print(f"Monólito -> pedidos: {pedidos_monolito} | tempo: {tempo_monolito:.2f}s")
print(f"Microsserviços -> pedidos: {pedidos_micro} | tempo: {tempo_micro:.2f}s")

