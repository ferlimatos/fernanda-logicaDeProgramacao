# Questão 9

compra_valor = float(input('Informe o valor de sua compra: R$'))

if compra_valor >= 500:
    print(f'Parabens, você ganhou um frete grátis e um brinde!')
    frete = 0
else:
    print('Parabéns, você ganhou um frete grátis.')

valor_total = compra_valor + frete

if compra_valor <= 50:
    if frete == 20:
        print(f'O valor do frete é de R${frete}. Portanto, o valor total que precisa ser pago é R${valor_total}')
else:
    frete > 10
    print(f'O valor do frete é de R${frete}. Portanto, o valor total que precisa ser pago é R${valor_total}')





