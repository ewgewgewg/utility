from flask import Flask
from threading import Thread
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def actions(data):

  @app.route('/')
  def home():
    return "Hello. I am alive!"

  @app.route('/show')
  def show():
    return data()

  def run():
    app.run(host='0.0.0.0',port=8080)


  t = Thread(target=run)
  t.start()