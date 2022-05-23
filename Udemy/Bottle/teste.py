from bottle import Bottle, run

app = Bottle()

msg = '''
<center><h1>Minha página web</h1></center>
<p>Python escreva pouco e faça muito!!!<p>
<center><a href="/Udemy_Python">Clique aqui</a></center>
'''

@app.route('/')
def index():
    return msg

@app.route('/Udemy_Python')
def curso():
    return '''
    <center><h1>Aprendi no Udemy, pvt.</h1></center>\
    <center><a href="/">Voltar a página anterior</a></center>
    '''

run(app, host='localhost', port = 8080)