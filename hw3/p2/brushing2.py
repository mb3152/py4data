# this .py file will accomplish the brushing for
# multidimensional datasets where viewing a 
# particular subset of data in many dimensions
# may be valueable for detecting clusters

## import relevant modules
import numpy as np 
import matplotlib.pyplot as plt
import numpy as np
import glob

# load up flower data
fileIN = 'flowers.csv'
# define data type
dt = np.dtype(dict(names=['sepal length','sepal width','petal length','petal width','species'],formats=[float,float,float,float,'S6']))
# load in, skipping the headers since we basically manually added them
data = np.loadtxt(fileIN,dtype=dt,delimiter=',',skiprows=1)

# ok, for right now we'll just make this particular to the flowers
# in the future, we need a way to load in data where the header
# names are the variable names
# get some data to colorize points
# not elegant
scolors = data['species']
scolors = list(scolors)
scolors = [s.replace('setosa', '#FF0000') for s in scolors]
scolors = [s.replace('versic', '#00FF00') for s in scolors]
scolors = [s.replace('virgin', '#0000FF') for s in scolors]

# get the size of this data set
ndims = len(data.dtype.names) - 1 #last row is not a dimension but a class

# get the number of examples in each dimensions
ndatapoints = len(data)

# set up the plots so there are enough to accomodate 
# every comparison
variables = data.dtype.names; variables = variables[:-1]
counter = 1
fig = plt.figure()
for Dvar in variables:
	for Ivar in variables:
		ax_cmd = 'ax' + str(counter) + ' = fig.add_subplot(ndims,ndims,counter)'
		exec  ax_cmd
		#ax = fig.add_subplot(ndims,ndims,counter)
		#ax.scatter(data[Ivar],data[Dvar],c=scolors)
		ax_cmd = 'ax' + str(counter) + '.scatter(data[Ivar],data[Dvar],c=scolors)'
		exec ax_cmd
		
		if Ivar == Dvar:
			ax_cmd = 'ax' + str(counter) + '.text(.1,.9,Ivar,horizontalalignment=\'left\',transform=ax' + str(counter) + '.transAxes)'
			eval(ax_cmd)
		#	ax.text(.1,.9,Ivar,horizontalalignment='left',transform=ax.transAxes)
		counter += 1
plt.show()




# copy/pasting the following from stack overflow for right now
from matplotlib.patches import Rectangle	

class Annotate(object):
    def __init__(self):
        self.ax = plt.gca()
        self.rect = Rectangle((0,0), 1, 1,fc='none',ec='b')
        self.x0 = None
        self.y0 = None
        self.x1 = None
        self.y1 = None
        self.ax.add_patch(self.rect)
        self.ax.figure.canvas.mpl_connect('button_press_event', self.which_axis)
        self.ax.figure.canvas.mpl_connect('button_press_event', self.on_press)
        self.ax.figure.canvas.mpl_connect('button_release_event', self.on_release)

    
    def which_axis(self, event):
        self.which_axis = event.inaxes
        axis0 ='Axes(0.125,0.726087;0.168478x0.173913)'
        axis1 ='Axes(0.327174,0.726087;0.168478x0.173913)'
        axis2 ='Axes(0.529348,0.726087;0.168478x0.173913)'
        axis3 ='Axes(0.731522,0.726087;0.168478x0.173913)'
        axis4 ='Axes(0.125,0.517391;0.168478x0.173913)'
        axis5 ='Axes(0.327174,0.517391;0.168478x0.173913)'
        axis6 ='Axes(0.529348,0.517391;0.168478x0.173913)'
        axis7 ='Axes(0.731522,0.517391;0.168478x0.173913)'
        axis8 ='Axes(0.125,0.308696;0.168478x0.173913)'
        axis9 ='Axes(0.327174,0.308696;0.168478x0.173913)'
        axis10 ='Axes(0.327174,0.308696;0.168478x0.173913)'
        axis11 ='Axes(0.529348,0.308696;0.168478x0.173913)'
        axis11 ='Axes(0.731522,0.308696;0.168478x0.173913)'
        axis12 ='Axes(0.125,0.1;0.168478x0.173913)'
        axis13 ='Axes(0.327174,0.1;0.168478x0.173913)'
        axis14 ='Axes(0.529348,0.1;0.168478x0.173913)'
        axis15 ='Axes(0.731522,0.1;0.168478x0.173913)'
        if str(event.inaxes) == axis0:
            print 'in axis1!'
        if str(event.inaxes) == axis1:
            print 'in axis2!'
        if str(event.inaxes) == axis2:
            print 'in axis3!'
        if str(event.inaxes) == axis3:
            print 'in axis4!'
        if str(event.inaxes) == axis4:
            print 'in axis5!'
        if str(event.inaxes) == axis5:
            print 'in axis6!'
        if str(event.inaxes) == axis6:
            print 'in axis7!'
        if str(event.inaxes) == axis7:
            print 'in axis8!'
        if str(event.inaxes) == axis8:
            print 'in axis9!'
        if str(event.inaxes) == axis9:
            print 'in axis10!'
        if str(event.inaxes) == axis10:
            print 'in axis11!'
        if str(event.inaxes) == axis11:
            print 'in axis12!'
        if str(event.inaxes) == axis12:
            print 'in axis13!'
        if str(event.inaxes) == axis13:
            print 'in axis14!'
        if str(event.inaxes) == axis14:
            print 'in axis15!'
        if str(event.inaxes) == axis15:
            print 'in axis16!'


    def on_press(self, event):
        self.x0 = event.xdata
        self.y0 = event.ydata
        print 'x1 is: ' + str(self.x0)
        print 'y1 is: ' + str(self.y0)

    def on_release(self, event):
        self.x1 = event.xdata
        self.y1 = event.ydata
        print 'x2 is: ' + str(self.x1)
        print 'y2 is: ' + str(self.y1)

a = Annotate()
plt.show()













