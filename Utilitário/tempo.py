from datetime import datetime
from datetime import date

tempo = datetime.now().strftime("%d.%m.%Y-%H:%M:%S")
print(tempo)

inicio = "09/11/2020"
print(inicio)

meu = datetime.strptime(inicio, '%d/%m/%Y').date()
print(meu)

dia = meu.strftime("%w")
print(dia)

d = meu.strftime("%U")
print(d)

e = "2020-W47"
r = datetime.strptime(e + '-0', "%Y-W%U-%w").date()
print(r)

anoInicio = int(meu.strftime("%Y"))
semanaInicio = int(d)
print(anoInicio)
print(semanaInicio)

semanaInicio += 69
print(semanaInicio)

while (semanaInicio > 53):
    semanaInicio -= 53
    anoInicio += 1
    
print(anoInicio)
print(semanaInicio)

texto = str(anoInicio)+'-W'+str(semanaInicio) #2022-W5
print(texto)
txt = datetime.strptime(texto + '-'+dia+'', "%Y-W%U-%w").date()
print(txt)
data = txt.strftime("%d/%m/%Y")
print(data)