# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 15:22:45 2019

@author: bguilfoyle
Overview: Create a polynomial based on user defined perameters with a GUI
"""

import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import ui
pi = np.pi
sin = np.sin
cos = np.cos
tan = np.tan
sinh = np.sinh
cosh = np.cosh
tanh = np.tanh

#==============================================================================
def makePlot(x, y):
	"""
    Overview: Make a plot of x vs y
    """
	plt.plot(x, y)
	plt.title("f(x) vs x")
	plt.xlabel("x")
	plt.ylabel("f(x)")
	plt.xlim(x[0], x[len(x) - 1])
	plt.ylim(min(y), max(y))
	plt.grid()

	b = BytesIO()
	plt.savefig(b)
	img = ui.Image.from_data(b.getvalue())
	img_view = ui.ImageView(background_color='white')
	img_view.content_mode = ui.CONTENT_SCALE_ASPECT_FIT
	img_view.image = img
	img_view.frame = (0, 0, 500, 500)
	img_view.present("sheet")


#==============================================================================


#==============================================================================
def fx(s):
	eq = []
	x1 = float(v["xLower"].text)
	x2 = float(v["xUpper"].text)
	for x in np.arange(x1, x2, (x2 - x1) / 1000):
		eq.append(eval(v["fOfx"].text))
	xRange = np.linspace(x1, x2, len(eq))
	makePlot(xRange, eq)


#==============================================================================

v = ui.load_view('fxCreator.pyui')
if min(ui.get_screen_size()) >= 768:
	# iPad
	v.frame = (0, 0, 250, 225)
	v.present('sheet')
else:
	# iPhone
	v.present(orientations=['portrait'])
