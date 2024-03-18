# import flask

from flask import Flask, render_template, jsonify
from database import load_animals_from_db

# create flask app
app = Flask (__name__)




# register a route to the application, here "/" means home page, after that the fuction 
# runs the scrpit to print the text
@app.route("/")

def hello_world():

  animalslist = load_animals_from_db()
  # sending database / dictionary to html, by passing argument below
  return render_template ('home-bs.html', animals=animalslist)

# now  to get list of animals using a json - jasonify returns the list as a json file - 
# it can be found at the route /api/animals
@app.route("/api/animals")
def list_animals():
  return jsonify(load_animals_from_db())
  


# this is to run the app
if __name__ == "__main__":
  # 0.0.0.0 to make it run locally
  # debug = true so that screen always changes
  app.run(host = '0.0.0.0', debug=True)