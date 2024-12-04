from flask import Flask
import helper
app = Flask(__name__)

@app.route('/')
#index route
@app.route('/index')
def index():
  return "<h1>Adopt a Pet!</h1>" + "<p>Browse through the links below to find your new furry friend:</p>" + "<ul><li><a href='/animals/dogs'>Dogs</li><li><a href='/animals/cats'>Cats</li><li><a href='/animals/rabbits'>Rabbits</li></ul>"