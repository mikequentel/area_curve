#!/usr/bin/python
from pylab import *

# rendering area
#figure(figsize=(4,2.5), dpi=80)
figure(figsize=(8,5), dpi=80)
#figure(figsize=(18,15), dpi=80)

# display area to use; can be modified to accomodate more graphs
subplot(111)

# range
#x = np.linspace(0, (2 * np.pi), 256,endpoint=True)
x = np.linspace(-10, 10, 256, endpoint=True)

# area poly range
xa = 1
xb = 11
area_poly_range = np.linspace(xa, xb, 256, endpoint=True)

# area poly
poly_range_dist = xb - xa
intervals = 10.0
panel_width = poly_range_dist/intervals
poly_x_origin = xa
poly_x_origin -= (poly_x_origin/2.0)
#poly = Rectangle((poly_x_origin, 0), panel_width, 1/(poly_x_origin + (poly_x_origin/2)), color='y')
poly = Rectangle((poly_x_origin, 0), panel_width, 1/xa, edgecolor='r', facecolor='r', alpha='0.5', linewidth='2')

# formulas to graph
sine = np.sin(x)
cosine = np.cos(x)
tangent = np.tan(x)
cotangent = 1/np.tan(x)
cosecant = 1/np.sin(x)
secant = 1/np.cos(x)

func = 1/x

# line styles and labels
#plot(x, sine, color="red", linewidth=2.5, linestyle="-",  label="sin")
#plot(x, cosine, color="blue", linewidth=2.5, linestyle="-",  label="cos")
#plot(x, tangent, color="orange", linewidth=2.5, linestyle="-", label="tan")
#plot(x, cotangent, color="purple", linewidth=2.5, linestyle="-", label="cot")
#plot(x, cosecant, color="green", linewidth=2.5, linestyle="-", label="csc")
#plot(x, secant, color="yellow", linewidth=2.5, linestyle="-", label="sec")
#plot(x, func, color="blue", linewidth=2.5, linestyle="-",  label="f(x) = 1/x")
plot(x, func, color="blue", linewidth=2.5, linestyle="-",  label="f(x) = 1/x")

# tick spines
ax = gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

# x tick limits and labels
#xlim(x.min()*1.1, x.max()*1.1)
#xticks([(-2 * np.pi), (-3 * np.pi/2), -np.pi, -np.pi/2, 0, np.pi/2, np.pi, (3 * np.pi/2), (2 * np.pi)], [r'$-2\pi$', r'$-3/2\pi$', r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$',  r'$3/2\pi$', r'$2\pi$'])
#xticks([-4, -3, -2, -1, +1, +2, +3, +4], [r'$-4$', r'$-3$', r'$-2$', r'$-1$', r'$+1$', r'$+2$', r'$+3$', r'$+4$'])

#x_tick_labels = []
#for i in range(-10, 11):
#  x_tick_labels.append(r'$' + str(i) + '$')
#xticks(range(-10, 11), x_tick_labels)

#x_tick_labels = []
#for i in range(-10, 11):
#  x_tick_labels.append(r'$' + str(i) + '$')
#xticks(range(-10, 11), x_tick_labels)

#x_tick_labels = []
#for i in x:
#  x_tick_labels.append(r'$' + str(i) + '$')
#xticks(x, x_tick_labels)


# x and y tick limits and labels
xy_range = range(-10, 11)
xlim(xy_range[0], xy_range[-1])
ylim(xy_range[0], xy_range[-1])
#yticks([-4, -3, -2, -1, +1, +2, +3, +4], [r'$-4$', r'$-3$', r'$-2$', r'$-1$', r'$+1$', r'$+2$', r'$+3$', r'$+4$'])
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
  #label.set_fontsize(16)
  label.set_fontsize(8)
  #label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65 ))
  label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.05))
  
# Polys
ax.add_patch(poly)

# display
show()
