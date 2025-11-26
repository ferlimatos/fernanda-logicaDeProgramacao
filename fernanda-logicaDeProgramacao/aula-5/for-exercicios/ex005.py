# Exercício 5

""" Crie um programa que peça ao usuário três valores: 
start, stop e step e utilize o range para gerar
uma sequência de números. O programa deve:
Mostrar todos os números gerados pelo range.
Calcular a soma de todos esses números e mostrar o total somado no final.
Dica: você precisará utilizar um acumulador para que
cada vez que um número seja impresso, ele seja adicionado ao valor total.
"""

var1 = int(input('Digite um número para ser start: '))
var2 = int(input('Digite um número para ser stop: '))
var3 = int(input('Digite um número para step: '))
soma = 0

# Mostrando os números gerados pelo range
print('Números no intervalo escolhido: ')

for numeros in range(var1, var2, var3):
    print(numeros, end=', ') 
    soma += numeros

# Resultado da soma total
print(f'A soma total dos números é: {soma}.')