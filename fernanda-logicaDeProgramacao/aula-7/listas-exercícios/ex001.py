# Exercício 1
# Crie uma lista vazia chamada numeros. Peça ao usuário para digitar 5 números e use append() para guardar todos na lista. Ao final, imprima a lista completa.

numeros = []

for i in range(5):
    entrada_str = input(f"Digite o {i+1}º número: ")
    try:
        numero_int = int(entrada_str)
    except ValueError:
        print("Entrada inválida! Usando 0 no lugar.")
        numero_int = 0

    numeros.append(numero_int)

print("\nSua lista de números completa:")
print(numeros)