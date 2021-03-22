codigo, qtd_itens = map(int, input().split(' '))
codigo_e_valor = {1: 4, 2: 4.5, 3: 5, 4: 2, 5: 1.5}

total_a_pagar = qtd_itens * codigo_e_valor[codigo]

print(f'Total: R$ {total_a_pagar:.2f}')
