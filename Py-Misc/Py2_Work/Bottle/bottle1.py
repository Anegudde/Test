from bottle import route, run
 
@route('/hello/:name')
def index(name='World'):
    return '<strong>Hello %s!</strong>' % name
 
run(host='10.137.235.57', port=8082)