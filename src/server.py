# Web Server.
# Serves the webpage, shows temp plots and temperature form.

import threading
import time
import io
from raspberry import Raspberry
from flask import Flask, Response, render_template, request

from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backends.backend_svg import FigureCanvasSVG
from matplotlib.figure import Figure

#import seaborn as sns
#sns.set()

app = Flask(__name__)

target_temp = 25


@app.route('/')
def index():
  #return str(d.getvalues())

  return render_template('test.html', 
                         current_temperature="{:.2f}".format(d.getValuesY()[-1]), 
                         target_temperature=target_temp,
                         resistor_state=r.getResistorState(),
                         avg_1="{:.2f}".format(r.getAverageXMinutes(1)),
                         avg_10="{:.2f}".format(r.getAverageXMinutes(10)),
                         avg_30="{:.2f}".format(r.getAverageXMinutes(30)))

@app.route('/settarget')
def setTarget():
  target_temperature = int(request.args.get("target_temperature", -1))
  if (target_temperature != -1):
    global target_temp
    target_temp = target_temperature
    r.setTartgetTemp(target_temp)
    print("settarget "+str(target_temp))
  return index()

@app.route("/plot.png")
def plot_png():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    x_points = range( d.getSize() )
    axis.plot(d.getValuesX(),d.getValuesY())

    output = io.BytesIO()
    FigureCanvasAgg(fig).print_png(output)
    return Response(output.getvalue(), mimetype="image/png")

def run(raspberry, database):
  global r 
  global d

  r = raspberry
  d = database

  app.run('0.0.0.0')
