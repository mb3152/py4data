#plots 6 motion parameters and the mean motion in MM from afni output of preproc_lesion.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import scipy

#hardcode in subject number and epi scan.
data = np.loadtxt('/home/despo/mb3152/data/Rest.LesionNew/Data/166/Rest/166-EPI-001-1D.txt')
data2 = np.loadtxt('/home/despo/mb3152/data/Rest.LesionNew/Data/166/Rest/166-EPI-001-MD1D.txt')
#plot that shit.
f, (ax1,ax2,ax3,ax4,ax5,ax6,ax7) = plt.subplots(7, sharex=True, sharey=True, squeeze = True)
ax1.plot(data[0:299,0],color='r')
ax2.plot(data[0:299,1],color='b')
ax3.plot(data[0:299,2],color='g')
ax4.plot(data[0:299,3],color='r')
ax5.plot(data[0:299,4],color='b')
ax6.plot(data[0:299,5],color='g')
ax1.set_title('Plotting Motion Parameters')
ax7.plot(data2, color ='r')
ax7.set_ylabel('Mean')
ax3.set_ylabel('6 Motion Parameters')
f.subplots_adjust(hspace=0)
plt.show()