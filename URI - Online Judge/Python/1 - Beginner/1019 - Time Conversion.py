tempo_seg = int(input())

horas = tempo_seg // 3600
minutos = (tempo_seg - horas * 3600) // 60
segundos = tempo_seg - horas * 3600 - minutos * 60

print(f'{horas}:{minutos}:{segundos}')
