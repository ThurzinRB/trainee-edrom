def direction (x,y, refX, refY):
    result =''
    if y > refY: result+='Cima'
    elif y<refY: result+='Baixo'

    if x<refX: result+= 'Esquerda'
    elif x > refX: result+='Direita'

    if result =='': result = 'Center'

    return result

