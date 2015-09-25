from bottle import get, static_file, run


@get('/static/<filename:path>')
def server_static(filename):
    # return static_file(filename, root='/home/leo/Documents')
    return static_file(filename, root='./')


run(host='localhost', port=8080, debug=True)
