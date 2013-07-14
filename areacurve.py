#!/usr/bin/python
from pylab import *

# makes area poly
def mkpolys(xa, xb, number_of_panels):
  # area poly range
  #xa = 1
  #xb = 11
  #area_poly_range = np.linspace(xa, xb, 256, endpoint=True)
  poly_range_dist = xb - xa
  #intervals = 10.0
  #intervals = number_of_panels
  #panel_width = poly_range_dist/intervals
  panel_width = poly_range_dist/number_of_panels
  #poly_x_origin = xa
  #poly_x_origin -= (poly_x_origin/2.0)
  half_panel = panel_width/2.0
  poly_list = []
  for i in range(xa, xb, int(panel_width)):
    panel_midpoint = i + half_panel
    #panel_midpoint = i
    #poly = Rectangle((i, 0), (panel_width + i), func(panel_midpoint), edgecolor='r', facecolor='r', alpha='0.5', linewidth='2')
    poly = Rectangle((i, 0), panel_width, func(panel_midpoint), edgecolor='r', facecolor='r', alpha='0.5', linewidth='2')
    poly_list.append(poly)
  return poly_list

def func(input_x):
  y = 0.05 * input_x**2
  return y

def main():
  # rendering area
  #figure(figsize=(4,2.5), dpi=80)
  #figure(figsize=(8,5), dpi=80)
  figure(figsize=(18,15), dpi=80)
  
  # display area to use; can be modified to accommodate more graphs
  subplot(111)
  
  # range
  #x = np.linspace(0, (2 * np.pi), 256,endpoint=True)
  x = np.linspace(-10, 10, 256, endpoint=True)
  # formula to graph
  #func = 1/x
  func_output = func(x)
  func_label = "0.05x^2"
  
  # line styles and labels
  plot(x, func_output, color="blue", linewidth=2.5, linestyle="-",  label=func_label)
  
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
  
  # legend
  legend(loc='upper left')
  
  for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(8)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.05))
    
  # Polys
  poly_list = mkpolys(1, 9, 4)
  for poly_item in poly_list:
    ax.add_patch(poly_item)
  
  # display
  show()

# Specifies name of main function.
if __name__ == "__main__":
  sys.exit(main())
    
