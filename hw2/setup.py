#! /usr/bin/env python 

from distutils.core import setup 

setup(name='grow',
      version='1.0',
      py_modules=['grow'],)

import os

#oct2py
os.system('pip install oct2py')
#homebrew
os.system('ruby -e "$(curl -kfsSL https://raw.github.com/mxcl/homebrew/go')

#Get Octave! 
os.system('brew tap homebrew/science')
os.system('brew update && brew upgrade')
os.system('brew install gfortran')
os.system('brew install octave')

#Get py2neo
os.system('pip install py2neo')
______________________________________________
#Get neo4j
os.system('brew install neo4j')

print 'Installation done!'

