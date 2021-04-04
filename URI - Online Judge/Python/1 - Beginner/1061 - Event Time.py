import datetime as dt

dia_inicio = input()
dia_inicio = int(dia_inicio[4:])
hora_inicio, minuto_inicio, segundo_inicio = map(int, input().split(' : '))

dia_final = input()
dia_final = int(dia_final[4:])
hora_final, minuto_final, segundo_final = map(int, input().split(' : '))

data_inicial = dt.datetime(2021, 4, dia_inicio, hora_inicio, minuto_inicio, segundo_inicio)
data_final = dt.datetime(2021, 4, dia_final, hora_final, minuto_final, segundo_final)

total_diferenca_segundos = (data_final - data_inicial).total_seconds()
total_dias = int(total_diferenca_segundos // 86400)
total_diferenca_segundos -= total_dias * 86400
total_horas = int(total_diferenca_segundos // 3600)
total_diferenca_segundos -= total_horas * 3600
total_minutos = int(total_diferenca_segundos // 60)
total_diferenca_segundos -= total_minutos * 60
total_segundos = int(total_diferenca_segundos)

print(f'{total_dias} dia(s)')
print(f'{total_horas} hora(s)')
print(f'{total_minutos} minuto(s)')
print(f'{total_segundos} segundo(s)')
