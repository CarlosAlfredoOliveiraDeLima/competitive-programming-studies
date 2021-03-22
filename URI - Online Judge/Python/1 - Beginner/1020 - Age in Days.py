dias_vividos = int(input())

anos = dias_vividos // 365
meses = (dias_vividos - anos * 365) // 30
dias = dias_vividos - anos * 365 - meses * 30

print(f'{anos} ano(s)\n{meses} mes(es)\n{dias} dia(s)')
