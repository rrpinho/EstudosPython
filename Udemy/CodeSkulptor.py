#http://www.codeskulptor.org/
#Desenvolvimento de games

import simplegui
import random
from math import sqrt

center_point = [50, 50]
radius = 20
window_width = 600 #Largaura
window_height = 400 #Altura
score = 0

#Desenha o canvas
def draw(canvas):
    canvas.draw_circle(center_point, radius, 1, 'Red', 'Red')

#Temporizador
def timer_handler():
    center_point[0] = random.randint(0, window_height)
    center_point[1] = random.randint(0, window_width)

#Ação de clique do mouse
def mouse_handler(pos):
    global score
    
    #Calculo da distância
    distance = sqrt(((pos[0] - center_point[0]) ** 2) +
                    ((pos[1] - center_point[1]) ** 2) )
    #Verifica se o usuário clicou dentro do circulo
    if distance < radius:
        score += 1 #Incremenda o score
    else:
        if score > 0:
            score -=1 #Decrementa o Score
    #Atualiza o campo da pontuação na janela
    label.set_text('Score: ' + str(score))

#Cria uma janela passando o titula, largura, altura
frame = simplegui.create_frame('Clique na bolinha', window_width, window_height)

#Cria um temporizador passando o intervalo e o manipulador
timer = simplegui.create_timer(1000, timer_handler)

#Seta os manipuladores de eventos
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouse_handler)

#Adiciona um label
label = frame.add_label('Score: ' + str(score))

timer.start() #Inicia o temporizador
frame.start() #Loop principal da aplicação