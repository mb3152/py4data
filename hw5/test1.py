from PIL import Image 
from scipy import ndimage
#from SimpleXMLRPCServer import SimpleXMLRPCServer
import SimpleXMLRPCServer
from skimage import data, img_as_float
from skimage import filter
from skimage.color import gray2rgb
from skimage.color import rgb2gray
from skimage.filter import sobel
from skimage.filter import threshold_otsu
from skimage.measure import structural_similarity as ssim
from xmlrpclib import Binary
import datetime
import logging
import matplotlib.pyplot as plt
import numpy as np
import os
import pylab
import skimage.io as io
import xmlrpclib
import xmlrpclib, sys


image = 'bassetts.jpg'
orig_image = io.imread(image)
image = io.imread(image)
image = rgb2gray(image)
io.imsave('black&white.jpg',image)
io.imsave('original.jpg',orig_image)
output1 = np.asarray(image)
output2 = np.asarray(orig_image)
io.concatenate_images(image,orig_image)