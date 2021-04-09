valores_positivos = 0
valor_para_media = 0
for i in range(6):
    aux = float(input())
    if aux > 0:
        valores_positivos += 1
        valor_para_media += aux

media = valor_para_media / valores_positivos
print(f'{valores_positivos} valores positivos')
print(f'{media:.1f}')

