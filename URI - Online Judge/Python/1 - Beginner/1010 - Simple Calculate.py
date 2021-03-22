codigo_1, qtd_1, valor_1 = map(float, input().split(' '))
codigo_2, qtd_2, valor_2 = map(float, input().split(' '))

valor_a_pagar = (qtd_1 * valor_1) + (qtd_2 * valor_2)

print('VALOR A PAGAR: R$ {:.2f}'.format(valor_a_pagar))