from bottle import route, run, template


@route('/hello')
@route('/hello/')
@route('/hello/<name>')
@route('/hello/<name:re:[a-z]+>/')
def greet(name='Stranger'):
    return template('<b>Hello {{name}}</b>!', name=name)


run(host='localhost', port=8080) 
