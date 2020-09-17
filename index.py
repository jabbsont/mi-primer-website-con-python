from flask import Flask, render_template

# Indica que estamos en la ruta principal atraves de un objeto
app = Flask(__name__)

# Nos permite crear una ruta
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Comprobamos si nos encontramos en la ruta principal
if __name__ == '__main__':
    app.run(debug=True) # Corre el servidor y en el modo debug, se refresca el servidor cada que se guardan los cambios