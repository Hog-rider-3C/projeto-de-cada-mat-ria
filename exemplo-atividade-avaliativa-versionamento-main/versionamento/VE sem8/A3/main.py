from monolitico import OnlineStore
from microsservicos import OnlineStoreMicro
from stress_test import run_test


TOTAL = 10


print("\n==============================")
print("TESTE DE CARGA")
print("==============================")
print(f"Pedidos simulados: {TOTAL}")


print("\n--- TESTANDO MONÓLITO ---")
mono = OnlineStore()
sucesso_mono, tempo_mono = run_test(mono, TOTAL)


print("\n--- TESTANDO MICROSSERVIÇOS ---")
micro = OnlineStoreMicro()
sucesso_micro, tempo_micro = run_test(micro, TOTAL)


print("\n==============================")
print("RESULTADO FINAL")
print("==============================")

print(
    f"Monólito -> "
    f"Pedidos: {sucesso_mono} | "
    f"Tempo: {tempo_mono:.2f}s"
)

print(
    f"Microsserviços -> "
    f"Pedidos: {sucesso_micro} | "
    f"Tempo: {tempo_micro:.2f}s"
)


if tempo_mono > tempo_micro:
    print("\nConclusão: Microsserviços teve melhor performance.")
else:
    print("\nConclusão: Performance semelhante.")