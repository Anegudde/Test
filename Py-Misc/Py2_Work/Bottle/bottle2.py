import os
from bottle import route, run, template

index_html = '''My first web app! By <strong>{{ author }}</strong>.'''


@route('/')
def index():
    return template(index_html, author='Real Python')


@route('/name/<name>')
def name(name):
    return template(index_html, author=name)

@route('/wiki/<pagename>')            # matches /wiki/Learning_Python
def show_wiki_page(pagename):
    pass
    
@route('/<action>/<user>')            # matches /follow/defnull
def user_api(action, user):
    if __name__ == '__main__':
        port = int(os.environ.get('PORT', 8082))
        run(host='0.0.0.0', port=port, debug=True)