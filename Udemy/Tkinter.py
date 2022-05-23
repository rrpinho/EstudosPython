#Interface gráfica

from tkinter import *

#Cria uma nova janela
window = Tk()

#Seta o título da janela
window.title('Meu Programa')

entry_text = Entry(window, width = 30) #Inicia uma entrada de texto
entry_text.pack() #Gerenciador de geometria
entry_text.focus_set() #Ao inicia o foco está nessa entrada

def clickButton():
    print(entry_text.get())

btn = Button(window, text = 'Clique aqui', width = 20, command = clickButton)
btn.pack()

window.geometry('300x150') #Tamanho da janela.

#Inicia a janela
window.mainloop()