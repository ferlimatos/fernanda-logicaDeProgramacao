# Sistema de notas escolares: receba a média do aluno e informe se foi aprovado, reprovado ou em recuperação.

# Média do aluno (float)
media = float(input("Informe a sua média: "))

# Se a média >= 7: Aprovado
# Senão, média >= 5: Recuperação
# Senão: Reprovado

if media >= 7:
  print("Parabéns, você foi aprovado!")
elif media >= 5:
  print("Você está de recuperação.")
else:
  print("Você está reprovado!")
