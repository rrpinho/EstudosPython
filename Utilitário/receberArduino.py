import serial
comunicacao = serial.Serial('/dev/ttyUSB0', 9600)
#comunicacao2 = serial.Serial('/dev/ttyACM0', 9600)


def limparRecebido(arduino):
    controle = False
    limpo = ''
    for letra in arduino:
        if letra == '\\':
            controle = False
            
        if controle:
            limpo += letra
            
        if letra == '\'':
            controle = True
    return limpo

while True:
    mystring = str(comunicacao.readline())
    recebido = limparRecebido(mystring)

    if recebido == 'Enviar':
        mensagem = 'ok'
        comunicacao.write(mensagem.encode())
    
    elif recebido[0:12] == '34-65-86/975':
        mensagem = 'Recebi'
        comunicacao.write(mensagem.encode())
        parametros = recebido
        
    print (recebido)
