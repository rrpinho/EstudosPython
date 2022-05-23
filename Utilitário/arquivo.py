'''
def escreverArquivo(texto):
    with open('/home/pi/Documents/Programacao/teste.txt', 'a') as arq:

        #Adicionar o dia e a hora no final de "texto".
        texto = texto + '\n'
    
        arq.write(texto)

        arq.close()

i = 0
while (i < 10):
    escreverArquivo('testando: ' + str(i))
    i = i + 1
'''
    
'''
with open('C:/Users/rrppi/Dropbox/Programação/Python/Aquaris/teste.txt', 'r') as arq:
        mystring = arq.readline()
        print (mystring)
        if (mystring == 'Ativar\n'):
            arq.close()
            with open('C:/Users/rrppi/Dropbox/Programação/Python/Aquaris/teste.txt', 'w') as arq:
                arq.write('')
        arq.close()
'''

def verificaArquivo(arquivo):
    with open('C:/Users/rrppi/Dropbox/Programação/Python/Aquaris/'+ arquivo +'.txt', 'r') as arq:
        mystring = arq.readline()
        print (mystring)
        if (mystring == 'Ativar\n'):
            arq.close()
            with open('C:/Users/rrppi/Dropbox/Programação/Python/Aquaris/'+ arquivo +'.txt', 'w') as arq:
                arq.write('')
        arq.close()
    return mystring

print (verificaArquivo('teste'))

'''
    r	Somente leitura
    w	Escrita, apagando (truncando) o conteúdo existente no arquivo
    a	Escrita, preservando o conteúdo existente (append). O arquivo é criado, se não existir. O texto é inserido no final do arquivo.
    b	Modo binário
    +	Abre o arquivo para atualização - leitura e escrita
    x	Abre o arquivo para criação exclusiva, falhando se o arquivo já existir.
    t	Modo de texto (padrão)
'''