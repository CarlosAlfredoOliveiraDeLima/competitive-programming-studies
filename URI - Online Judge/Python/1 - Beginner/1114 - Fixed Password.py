while True:
    login = 'Acesso Permitido' if int(input()) == 2002 else 'Senha Invalida'
    if login == 'Acesso Permitido':
        print(login)
        break
    else:
        print(login)
