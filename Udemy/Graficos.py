'''
    pip install matplotlib
'''
# MatPlotLib - Plotar Gráficos

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [0.5, 1.6, 3.4, 4.5, 6.7, 8.8]
x1 = [0.2, 0.5, 0.7, 1]
y1 = [-1, -2, -3, -4]
plt.plot(x, y, 'g') #Linha verde, ou r para linha vermelha
plt.plot(x1, y1, 'ro') #ro == Pontos vermelho - R vermelho - O Ponto
plt.ylabel('Eixo Y')
plt.xlabel('Eixo X')

plt.show()