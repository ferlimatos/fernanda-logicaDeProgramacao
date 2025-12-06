# Tabuada automática: o usuário digita um número e o programa mostra a tabuada completa.

numero = int(input("Digite um número para ver a tabuada: "))

print(f'Tabuada de  {numero}:')

for i in range(1, 11, 1):
    print(f"{numero} x {i} = {numero * i}")