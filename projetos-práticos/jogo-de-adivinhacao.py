# Jogo de adivinhação: o programa escolhe um número secreto e o usuário tenta adivinhar.

import random

# Configurações iniciais
numero_secreto = random.randint(0,100)
limite_tentativas = 5
contador = 1

palpite = int(input("Qual é o seu palpite? "))

# Loop de tentativas
while palpite != numero_secreto and contador < limite_tentativas:
  if palpite > numero_secreto:
    print("O número secreto é menor. Tente outra vez.")
  else:
    print("O número secreto é maior. Tente outra vez.")
  # Mostrar quantas tentativas restam
  print(f"Você ainda tem {limite_tentativas - contador} tentativas.")
  # Novo palpite
  palpite = int(input("Qual é o seu novo palpite? "))
  contador += 1

# Fim do jogo
if palpite == numero_secreto:
  print(f"Parabéns, você acertou o número secreto! Foram feitas {contador} tentativas.")
else:
  print(f"Você não conseguiu adivinhar o número secreto que era {numero_secreto}.")