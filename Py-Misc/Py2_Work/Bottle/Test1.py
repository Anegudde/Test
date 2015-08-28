from bottle import Bottle, run, template, route
app = Bottle()

@app.route('/hello')
def hello():
    return "Hello World!"


@route('/hello/name')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)

run(app, host='0.0.0.0', port=8081)