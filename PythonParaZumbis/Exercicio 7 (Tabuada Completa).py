#Imprima as tabuadas de 1 à 10
tabuada = 1
while tabuada <=10:
    n=1
    print("Tabuada de: %d" %tabuada)
    while n<=10:
        print("%d x %d = %d" %(tabuada, n, tabuada*n))
        n=n+1
    tabuada = tabuada+1
