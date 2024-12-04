from flask import Flask
import helper
app = Flask(__name__)

@app.route('/')
#index route
@app.route('/index')
def index():
  return "<h1>Adopt a Pet!</h1>" + "<p>Browse through the links below to find your new furry friend:</p>" + "<ul><li><a href='/animals/dogs'>Dogs</li><li><a href='/animals/cats'>Cats</li><li><a href='/animals/rabbits'>Rabbits</li></ul>"

@app.route('/animals/<pet_type>')
def animals(pet_type):
  html = ''
  matching_pets_list = helper.pets.get(pet_type)
  html += "<ul>"
  #Display all pet names of the given pet type
  for i, pets in enumerate(matching_pets_list):
    html += "<li><a href= '/animals/{}/{}'>{}</l1>".format(pet_type, i, matching_pets_list[i].get('name'))
  html += "</ul>"
  return html

@app.route('/animals/<pet_type>/<pet_id>')
def pet(pet_type, pet_id):
  #Retrieve pet profile
  index = int(pet_id)
  matching_pets_list = helper.pets.get(pet_type)
  pet_profile = matching_pets_list[index]
  html = "<h1>{}</h1><img src={}><p>{}</p><ul><li>{}</li><li>{} year(s) old</li></ul>".format(pet_profile.get('name'), pet_profile.get('url'), pet_profile.get('description'), pet_profile.get('breed'), pet_profile.get('age'))
  return html
