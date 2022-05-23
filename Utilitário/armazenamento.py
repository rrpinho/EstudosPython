mystring = '34-65-86/975&1&23.45&7.12&0.53&2.58&12.54&254.12&12.2&14&231&04.04.2018-17:54:32'
mystring2 = '34-65-86/975&2&22.36&6.68&1.24&1.23&11.45&382.66&16.8&23&126&05.04.2018-11:50:45'

token = 'token-8I2B4M7D4P1P9E-maq-waterfarmmaq'

mylist = []
armazenamento = {}

armazenamento['key'] = []
armazenamento['eg'] = []
armazenamento['tp'] = []
armazenamento['ph'] = []
armazenamento['tb'] = []
armazenamento['nv'] = []
armazenamento['or'] = []
armazenamento['ct'] = []
armazenamento['sl'] = []
armazenamento['vz'] = []
armazenamento['nh'] = []
armazenamento['tm'] = []


mylist = mystring.split('&')
for key in armazenamento:
    if ( key == 'key'):
        armazenamento[key].append(mylist[0])
        
    elif ( key == 'eg'):
        armazenamento[key].append(mylist[1])
        
    elif ( key == 'tp'):
        armazenamento[key].append(mylist[2])

    elif ( key == 'ph'):
        armazenamento[key].append(mylist[3])
        
    elif ( key == 'tb'):
        armazenamento[key].append(mylist[4])

    elif ( key == 'nv'):
        armazenamento[key].append(mylist[5])

    elif ( key == 'or'):
        armazenamento[key].append(mylist[6])

    elif ( key == 'ct'):
        armazenamento[key].append(mylist[7])

    elif ( key == 'sl'):
        armazenamento[key].append(mylist[8])

    elif ( key == 'vz'):
        armazenamento[key].append(mylist[9])

    elif ( key == 'nh'):
        armazenamento[key].append(mylist[10])

    elif ( key == 'tm'):
        armazenamento[key].append(mylist[11])



mylist = mystring2.split('&')
for key in armazenamento:
    if ( key == 'key'):
        armazenamento[key].append(mylist[0])
        
    elif ( key == 'eg'):
        armazenamento[key].append(mylist[1])
        
    elif ( key == 'tp'):
        armazenamento[key].append(mylist[2])

    elif ( key == 'ph'):
        armazenamento[key].append(mylist[3])
        
    elif ( key == 'tb'):
        armazenamento[key].append(mylist[4])

    elif ( key == 'nv'):
        armazenamento[key].append(mylist[5])

    elif ( key == 'or'):
        armazenamento[key].append(mylist[6])

    elif ( key == 'ct'):
        armazenamento[key].append(mylist[7])

    elif ( key == 'sl'):
        armazenamento[key].append(mylist[8])

    elif ( key == 'vz'):
        armazenamento[key].append(mylist[9])

    elif ( key == 'nh'):
        armazenamento[key].append(mylist[10])

    elif ( key == 'tm'):
        armazenamento[key].append(mylist[11])

print (armazenamento)
print (len(armazenamento))
print (armazenamento.items())
print (len(armazenamento.items()))
print (armazenamento.values())
print (len(armazenamento.values()))
print (armazenamento.keys())
print (len(armazenamento.keys()))

'''
print (len(armazenamento['tm']))
armazenamento['tm'].pop(0)
print (armazenamento['tm'])
print (len(armazenamento['tm']))
ultimalinha = 0
ultimalinha = len(armazenamento['tm']) - 1
print (ultimalinha)
'''

print (armazenamento['ph'][0])

def ultimaLinha():
    return (len(armazenamento['nh']) - 1)   
linha = ultimaLinha()
print (linha)
print (type(linha))
for key in armazenamento:
    armazenamento[key].pop(linha)
print (armazenamento)