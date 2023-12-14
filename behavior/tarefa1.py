def direction (x,y):
    result =''
    if y > 0: result+='Cima'
    elif y<0: result+='Baixo'

    if x<0: result+= 'Esquerda'
    elif x > 0: result+='Direita'

    if result =='': result = 'Center'

    return result

