from flask import Flask
#from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello there beautiful people!</h1>'


@app.route('/information') #this is an example of routing
def info():
    return '<h1>this is the information page!</h1>'


@app.route('/page/<name>')
def page(name):
    # Page for an individual page.
    return '<h1>This is a page for {}<h1>'.format(name)
    #return "Upper case: {}".format(name.upper())
    #return "100th letter: {}".format(name[100])


if __name__ == '__main__':
    app.run(debug=True)



# @app.route('/')
# def index():
#     # Grab the visitors User Agent information
#     browser_info = request.headers.get('User-Agent')
#     return '<h2>Here is your browser info:</h2> <p>{}</p>'.format(browser_info)


# @app.route('/')
# def index():
#     # Welcome Page
#     return "<h1>Welcome! Go to /puppy_latin/name to see your name in puppy latin!</h1>"

# @app.route('/puppy_latin/<name>')
# def puppylatin(name):
#     # Puppy Latin the name that comes in!
#     pupname = ''
#     if name[-1]=='y':
#         pupname = name[:-1]+'iful'
#     else:
#         pupname = name+'y'

#     return "<h1>Hi {}! Your puppylatin name is {} </h1>".format(name,pupname)

