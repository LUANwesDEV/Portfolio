from flask import Flask, render_template, redirect  #Rodar um arquivo HTML

app = Flask(__name__) # "app" - Variavel que vai receber o objeto Flask e sinalizar que vai usar o abjeto no arquivo "main"

@app.route('/')# Para te fato o programa rodar
def index(): # Função - Para rodar o arquivo principal.
    return render_template('index.html')


if __name__ == '__main__': # Quero que ele "rode" só se estiver no arquivo "main"
    app.run(debug=True) # Vai rodar a aplicação/ debug=True - vai rodar a aplição sem precisar atualizar o codigo.

    