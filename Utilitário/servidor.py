from flask import Flask

app = Flask(__name__)

#with open('C:/Users/rrppi/Dropbox/Programação/Python/Aquaris/reguladorOxigenio.txt', 'w') as arq:

@app.route('/ro')
def ro():
    with open('/home/pi/Documents/Programacao/Aquaris/reguladorOxigenio.txt', 'w') as arq:
        arq.write('Ativar\n')
        arq.close()

    return 'Ativar o Regulador de Oxigênio'

@app.route('/ra')
def ra():
    with open('/home/pi/Documents/Programacao/Aquaris/reguladorComida.txt', 'w') as arq:
        arq.write('Ativar\n')
        arq.close()

    return 'Ativar o Regulador de Comida'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')