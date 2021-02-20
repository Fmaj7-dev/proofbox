# Web Server.
# Serves the webpage, shows temp plots and temperature form.

import threading
import time
from raspberry import Raspberry
from flask import Flask
app = Flask(__name__)

r=[]

@app.route('/')
def index():
  return str(r.getTemp())

def run(raspberry):
  global r 
  r = raspberry
  app.run()
