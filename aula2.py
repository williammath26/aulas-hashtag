def descobrir_servidor(email):
    try:
        posicao_a = email.index('@')
    
        servidor = email[posicao_a:]
        if 'gmail' in servidor:
            return 'gmail'
        elif 'hotmail' in servidor or 'outlook' in servidor or 'live' in servidor:
            return 'hotmail'
        elif 'yahoo' in servidor:
            return 'yahoo'
        elif 'uol' in servidor or 'bol' in servidor:
            return 'uol'
        else:
            return 'Não Determinado'
    except:
        print('Email digitado não tem @,tente novamente')
    
email = input("qual seu email?")
print(descobrir_servidor(email))
    