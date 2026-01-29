from bokeh.io import curdoc
from bokeh.plotting import figure
from random import random

p = figure(title="Live Updating Graph")
line = p.line([], [], line_width=2)

x, y = [], []

def update():
    x.append(len(x))
    y.append(random())
    line.data_source.data = {"x": x, "y": y}

curdoc().add_periodic_callback(update, 500)
curdoc().add_root(p)
