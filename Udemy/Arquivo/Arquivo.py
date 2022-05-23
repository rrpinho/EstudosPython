# Manipulando arquivos

# Abrir um arquivo para escrita
arq = open('arquivo.txt', 'w')
# Mensagem que será escrita no arquivo
msg = '''Esse eh um exemplo
de mensagem que irei escrever
no arquivo
'''
#Escrevendo no arquivo
arq.write(msg)
#Fechando o arquivo
arq.close()

#Abrindo o arquivo para leitura
arq = open('arquivo.txt', 'r')
# Imprimindo o texto do arquivo
print(''.join(linha for linha in arq.readlines()))
#Fechando arquivo
arq.close()