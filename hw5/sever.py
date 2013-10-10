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
import pickle


class ImageService:

	def test(self):
		"""Simple function to respond when called to demonstrate connectivity."""
		return str("You are connected to Maxwell's Lossless Image Manipulator")

	def color2black(self,image):
		orig_image = io.imread(image)
		image = io.imread(image)
		image = rgb2gray(image)
		io.imsave('black&white.jpg',image)
		io.imsave('original.jpg',orig_image)
        data = pickle.dumps(image)
        return data

	def detectedges(self,image):
		"""Sorbel edge detector"""
		orig_image = io.imread(image)
		image = io.imread(image)
		image = rgb2gray(image)
		edge_sobel = sobel(image)
		io.imsave('edges.jpg',edge_sobel)
		io.imsave('original.jpg',orig_image)
		return 'edges.jpg'
		return 'original.jpg'
		
	def brighten(self,image):
		orig_image = io.imread(image)
		image = Image.open(image)
		image = image.point(lambda p: p * 3)
		image.save('brightened.jpg')
		io.imsave('original.jpg',orig_image)
		return 'brightened.jpg'
		return 'original.jpg'

host, port = "", 5025
server = SimpleXMLRPCServer.SimpleXMLRPCServer((host, port), allow_none=True)
server.register_instance(ImageService())
#server = SimpleXMLRPCServer(('localhost', 9000), logRequests=True, allow_none=True) #for local connections

server.register_introspection_functions()
server.register_multicall_functions()
 
try:
    print 'Use Control-C to exit'
    server.serve_forever()
except KeyboardInterrupt:
    print 'Exiting'

server.serve_forever()