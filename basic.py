from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello there beautiful people!</h1>'


@app.route('/information') #this is an example of routing
def info():
    return '<h1>this is the information page!</h1>'

@app.route('/page/<name>')
def page(name):
    # Page for an individual puppy.
    return '<h1>This is a page for {}<h1>'.format(name)
if __name__ == '__main__':
    app.run()
