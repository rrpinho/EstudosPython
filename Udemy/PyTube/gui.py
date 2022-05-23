from tkinter import *
from downloader import *

window = Tk()
window.title('Youtube Downloader')
window.geometry('500x200')
window.resizable(0,0)

title = Label(window, text='Youtube Downloader', font=('Arial', 25), fg='Blue')
title.pack()

msg = Label(window, width=60, justify='center')

entry_url = Entry(window, width=60, justify='center')
entry_url.insert(0, 'Enter the URL')
entry_url.pack()
entry_url.focus_set()

entry_name_video = Entry(window, width=60, justify='center')
entry_name_video.insert(0, 'Enter the name video')
entry_name_video.pack()

#Função para o evento de clique de botão
def click_button():
    #Obtém os textos
    url = entry_url.get()
    name_video = entry_name_video.get()

    if download_video(url, name_video):
        msg['fg'] = 'Green'
        msg['text'] = 'Download feito com sucesso!'
    else:
        msg['fg'] = 'Red'
        msg['text'] = 'Ocorreu alguma falha... :('

btn = Button(window, text='Download now', width=20, command=click_button)
btn.pack()

msg.pack()

window.mainloop()