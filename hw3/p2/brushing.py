
## import relevant modules
import numpy as np 
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import glob
import pandas as pd
from matplotlib.patches import Rectangle



class FlowerBrusher(object):

    """Make an interactive brush plot from data in a CSV file.

    Clicking and dragging on the plot updates which datapoints are
    highlighted.

    """
    def __init__(self, csv_file):
        """Initialize the plot.

        Inputs
        ------
        csv_file : string
            
            Path to the CSV file to be loaded.  Each column in the file
            should represent a different dimension of the data, and the
            rows should be different observations.

            The last column in the CSV file is used to set the colors of
            the datapoints in the plot, and therefore it must have a
            maximum of eight or fewer unique values (only eight colors
            are supported).

        """
        plt.close('all') 
        self.df = pd.read_csv(csv_file)
        values_to_color = list(set(self.df[self.df.columns[-1]]))
        values_to_color.sort()
        colors = ['b', 'orange', 'g', 'r', 'c', 'm', 'y', 'b']
        if len(values_to_color) > len(colors):
            raise ValueError('Too many unique values in last column of ' +
                             'DataFrame')
        color_dict = {value: colors[i] for i, value in
                      enumerate(values_to_color)}
        # The last dimension will be used to set the colors of the
        # datapoints, and therefore will not receive its own set of subplots.
        self.n_dims = self.df.shape[-1] - 1
        f, self.ax_array = plt.subplots(self.n_dims, self.n_dims)
        self.datapoint_colors = np.array([color_dict[s] for s in
                                          self.df[self.df.columns[-1]]])
        # Initialize array for storing scatterplots.
        self.plots = np.empty((self.n_dims, self.n_dims),
                              dtype=matplotlib.collections.PathCollection)
        for i in xrange(self.n_dims):
            for j in xrange(self.n_dims):
                self.ax = self.ax_array[i, j]
                # Instead of taking index j for the x-data, take n_dims - (j +
                # 1).  This is just to be consistent with the mbostock
                # arrangement of subplots.
                self.plots[i, j] = self.ax.scatter(
                    self.df[self.df.columns[self.n_dims - (j + 1)]],
                    self.df[self.df.columns[i]],
                    color=self.datapoint_colors)
                self.ax.set_xlabel(self.df.columns[self.n_dims - (j + 1)])
                self.ax.set_ylabel(self.df.columns[i])
                # So labels are less cluttered, only make y-axis
                # labels down the left column visible, and only make
                # x-axis labels along the bottom row visible.
                if i != self.n_dims - 1:
                    self.ax.get_xaxis().set_visible(False)
                if j != 0:
                    self.ax.get_yaxis().set_visible(False)
        # Keep track of whether mouse is pressed.
        self.pressed = False
        # Initialize the rectangle to have 0 height and width, so it's
        # invisible (and anyway, don't draw it).
        self.rect = Rectangle((0, 0), 0, 0, alpha=0.5, color='0.5')
        f.canvas.mpl_connect('button_press_event', self.on_press)
        f.canvas.mpl_connect('motion_notify_event', self.on_motion)
        f.canvas.mpl_connect('button_release_event', self.on_release)
        # It's important that show be called at the very end of all
        # this setup (I've learned from trial-and-error).
        f.show()

    def on_press(self, event):
        # Erase the previous rectangle.
        self.rect.set_width(0)
        self.rect.set_height(0)
        self.pressed = True
        self.ax = event.inaxes
        self.x0 = event.xdata
        self.y0 = event.ydata
        # Re-initialize the rectangle to have 0 height and width.
        self.rect = Rectangle((self.x0, self.y0), 0, 0, alpha=0.5, color='0.5')
        self.ax.add_patch(self.rect)
        
    def on_motion(self, event):
        if self.pressed:
            # Update the rectangle.
            self.x1 = event.xdata
            self.y1 = event.ydata
            new_width = self.x1 - self.x0
            new_height = self.y1 - self.y0
            self.rect.set_width(new_width)
            self.rect.set_height(new_height)
            # Find the datapoints outside the rectangle.  Take
            # advantage of the fact that the axis labels are the same
            # as the column labels in self.df.
            x_column = self.ax.get_xlabel()
            y_column = self.ax.get_ylabel()
            min_x, max_x = np.min([self.x0, self.x1]), np.max([self.x0,
                                                               self.x1])
            min_y, max_y = np.min([self.y0, self.y1]), np.max([self.y0,
                                                               self.y1])
            titleminx = "%.2f" % (min_x)+ '"'
            titlemaxx = "%.2f" % (max_x)+ '"'
            titleminy = "%.2f" % (min_y)+ '"'
            titlemaxy = "%.2f" % (max_y)+ '"'
            titlex=str(x_column)
            titley=str(y_column)
            print 'Plotting ' + titlex + ' from ' + titleminx + ' to ' + titlemaxx + ' and ' + titley + ' from ' + titlemaxx + ' to ' + titlemaxy
            # Update the datapoint colors, by setting everything
            # outside the rectangle bounds to gray.
            updated_colors = self.datapoint_colors.copy()
            
            if new_width and new_height:
                # Gray out colors only if the rectangle really exists.
                updated_colors[
                    np.logical_or(np.logical_or(np.logical_or(
                                self.df[x_column] < min_x,
                                self.df[x_column] > max_x),
                                                self.df[y_column] < min_y),
                                  self.df[y_column] > max_y)] = '0.75'
            for i in xrange(self.n_dims):
                for j in xrange(self.n_dims):
                    self.plots[i, j].set_color(updated_colors)
            self.ax.figure.canvas.draw()
            self.ax.figure.canvas.set_window_title('Plotting ' + titlex + ' from ' + titleminx + ' to ' + titlemaxx + ' and ' + titley + ' from ' + titlemaxx + ' to ' + titlemaxy)


    def on_release(self, event):
        # Update the rectangle one last time and then set the mouse press off.
        self.on_motion(event)
        self.pressed = False


if __name__ == '__main__':
    a = FlowerBrusher('flowers.csv')













