# Exercício 4

# Crie uma tabuada utilizando step, onde o usuário
# deve digitar a razão da tabuada.

razao = int(input('Digite a razão da tabuada: '))

print(f'Tabuada de  {razao}:')

for i in range(razao, razao * 11, razao):

    print(i)
