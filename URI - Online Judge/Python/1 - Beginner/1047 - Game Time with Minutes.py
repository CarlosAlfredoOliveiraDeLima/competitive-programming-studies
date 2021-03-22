hora_inicial, minutos_iniciais, hora_final, minutos_finais = map(int, input().split())

if hora_inicial <= hora_final and minutos_iniciais < minutos_finais:
    total_horas = hora_final - hora_inicial
    total_minutos = minutos_finais - minutos_iniciais
elif hora_inicial < hora_final and minutos_iniciais > minutos_finais:
    total_horas = (hora_final - hora_inicial) - 1
    total_minutos = minutos_finais - minutos_iniciais + 60
elif hora_inicial > hora_final and minutos_iniciais < minutos_finais:
    total_horas = (24 - hora_inicial) + hora_final
    total_minutos = minutos_finais - minutos_iniciais
elif hora_inicial >= hora_final and minutos_iniciais > minutos_finais:
    total_horas = (24 - hora_inicial) + hora_final - 1
    total_minutos = 60 + minutos_finais - minutos_iniciais
else:
    total_horas = 24
    total_minutos = 0

print(f'O JOGO DUROU {total_horas} HORA(S) E {total_minutos} MINUTO(S)')