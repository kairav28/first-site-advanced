# import flask
from flask import Flask, render_template

# create flask app
app = Flask (__name__)

# register a route to the application, here "/" means home page, after that the fuction runs the scrpit to print the text
@app.route("/")

def hello_world():
  return render_template ('home.html')


# this is to run the app
if __name__ == "__main__":
  # 0.0.0.0 to make it run locally
  # debug = true so that screen always changes
  app.run(host = '0.0.0.0', debug=True)