# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 20:43:29 2021

@author: zhill
"""

from wx.tools import img2py
 
image_file = 'images/alien.bmp'
image_file2 = 'images/ship.bmp'

python_file = 'python_alien.py'
python_file2 = 'python_ship.py'
 
img2py.img2py(image_file=image_file, python_file=python_file,
              imgName='get_python_alien', icon=True)

img2py.img2py(image_file=image_file2, python_file=python_file2,
              imgName='get_python_ship', icon=True)