from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.models import Slider
from bokeh.layouts import column

# Make a simple plot
p = figure(title="Circle Size Slider")
r = p.circle([1], [1], size=10, color="navy")  # a single circle

# Create a slider widget
slider = Slider(start=5, end=50, value=10, step=1, title="Circle Size")

# The callback function
def update(attr, old, new):
    r.glyph.size = slider.value    # update circle size

slider.on_change("value", update)

# Layout
layout = column(slider, p)

# Add to document
curdoc().add_root(layout)
