import string

qtd_testes = int(input())
alfabeto = string.ascii_uppercase

for i in range(qtd_testes):
    soma = 0
    qtd_analises = int(input())
    for j in range(qtd_analises):
        string = input()
        contador = 0
        for h in range(len(string)):
            soma += alfabeto.index(string[h]) + j + contador
            contador += 1
    print(soma)
