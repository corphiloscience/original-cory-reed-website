from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cakes')
def cakes():
    return render_template('cakes.html')

# Dynamic routes
@app.route('/cakes/<name>')
def hello(name):
    return render_template('cakes.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')