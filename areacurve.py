#!/usr/bin/python
from scipy import integrate
from pylab import *
xa = 1
xb = 10
samples = 22
poly_data = []
poly_list = []
area_text = None
exact_area = 0.0
exact_area_text = None
xa_text = None
xb_text = None

# makes area poly
def mkpolys(xa, xb, number_of_panels):
  global exact_area
  # area poly range
  poly_range_dist = (xb - xa) * 1.0
  panel_width = poly_range_dist / number_of_panels
  half_panel = panel_width / 2.0
  poly_list = []
  area = 0.0
  poly_data = []
  exact_area = integrate.quad(lambda x: func(x), xa, xb)[0]

  for i in np.arange(xa, xb, panel_width):
    panel_midpoint = i + half_panel
    panel_height = func(panel_midpoint)
    poly = Rectangle((i, 0), panel_width, panel_height, edgecolor='r', facecolor='r', alpha='0.5', linewidth='2')
    poly_list.append(poly)
    area += (panel_width * panel_height)
  
  poly_data.append(poly_list)
  poly_data.append(area)
  return poly_data

def init(samples):
  global poly_data
  #poly_data = mkpolys(start, stop, samples)
  poly_data = mkpolys(xa, xb, samples)

def func(input_x):
  y = 0.05 * input_x ** 2
  #y = (input_x - 3) * (input_x - 5) * (input_x - 7) + 85
  return y

#################### START GUI CONTROLS ######################################

# Class DiscreteSlider from Joe Kington on Stackoverflow at thread:
# http://stackoverflow.com/questions/13656387/can-i-make-matplotlib-sliders-more-discrete
class DiscreteSlider(Slider):
  """A matplotlib slider widget with discrete steps."""
  def __init__(self, *args, **kwargs):
    """Identical to Slider.__init__, except for the "increment" kwarg.
    "increment" specifies the step size that the slider will be discritized
    to."""
    #self.inc = kwargs.pop('increment', 0.5)
    self.inc = kwargs.pop('increment', 1)
    Slider.__init__(self, *args, **kwargs)

  def set_val(self, val):
    discrete_val = int(val / self.inc) * self.inc
    # We can't just call Slider.set_val(self, discrete_val), because this 
    # will prevent the slider from updating properly (it will get stuck at
    # the first step and not "slide"). Instead, we'll keep track of the
    # the continuous value as self.val and pass in the discrete value to
    # everything else.
    xy = self.poly.xy
    xy[2] = discrete_val, 1
    xy[3] = discrete_val, 0
    self.poly.xy = xy
    self.valtext.set_text(self.valfmt % discrete_val)
    if self.drawon: 
      self.ax.figure.canvas.draw()
    self.val = val
    if not self.eventson: 
      return
    for cid, func in self.observers.iteritems():
      func(discrete_val)

#################### END GUI CONTROLS ########################################

def update(val, s=None):
  global poly_data
  global exact_area_text
  global area_text
  global xa_text
  global xb_text
  if poly_data:
    if len(poly_data) > 0:
      poly_list = poly_data[0]
      for poly_item in poly_list:
        poly_item.remove()
  poly_data = mkpolys(xa, xb, val)
  poly_list = poly_data[0]
  total_area = poly_data[1]
  for poly_item in poly_list:
    ax.add_patch(poly_item)
  #print total_area
  if xa_text is not None:
    xa_text.remove()
  if xb_text is not None:
    xb_text.remove()
  if exact_area_text is not None:
    exact_area_text.remove()
  if area_text is not None:
    area_text.remove()
  xa_text = plt.text(2.0, 5.0, "xa: " + str(xa))
  xb_text = plt.text(12.5, 5.0, "xb: " + str(xb))
  exact_area_text = plt.text(2.0, 3.5, "Exact Area: " + str(exact_area))
  area_text = plt.text(2.0, 2.0, "Riemann Sum Area: " + str(total_area))
  draw()
  return poly_data

# rendering area
#figure(figsize=(4,2.5), dpi=80)
figure(figsize=(8,5), dpi=80)
#figure(figsize=(18, 15), dpi=80)

# display area to use; can be modified to accommodate more graphs
subplot(111)

# range
x = np.linspace(-10.0, 10.0, 256, endpoint=True)

# tick spines
ax = gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

# x and y tick limits and labels
xy_range = range(-10, 11)
xlim(xy_range[0], xy_range[-1])
ylim(xy_range[0], xy_range[-1])
x_tick_labels = []
y_tick_labels = []
for i in xy_range:
  x_tick_labels.append(r'$' + str(i) + '$')
  y_tick_labels.append(r'$' + str(i) + '$')
xticks(xy_range, x_tick_labels)
yticks(xy_range, y_tick_labels)

for label in ax.get_xticklabels() + ax.get_yticklabels():
  label.set_fontsize(9)
  label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.05))

# Polys
poly_data = update(samples)

# formula to graph
#func = 1/x
func_output = func(x)
#func_label = area_label + "\nPanels: " + str(samples)
func_label = "func(x)"

# line styles and labels
plot(x, func_output, color="blue", linewidth=2.5, linestyle="-", label=func_label)

# legend
legend(loc='upper left')

# gui controls
plt.subplots_adjust(left=0.25, bottom=0.25)
slider_min = 1
slider_max = 100
axcolor = 'white'
panel_axis  = plt.axes([0.25, 0.05, 0.65, 0.03], axisbg=axcolor)
s_panels = DiscreteSlider(panel_axis, 'Panels', valinit=slider_min, valmin=slider_min, valmax=slider_max, valfmt='%3.0f', facecolor='green', increment=1)
s_panels.on_changed(update)
s_panels.set_val(samples)

# display
show()
