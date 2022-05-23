moedas = [100, 50, 20, 10, 5, 1]
sol = []
soma = 0
troco = 21
i = 0
cont = 0
while i < len(moedas) and soma != troco:
    cont += 1
    if soma + moedas[i] <= troco:
        sol.append(moedas[i])
        soma += moedas[i]
    else:
        i += 1

    if soma == troco:
        break
print(sol)
print(cont)