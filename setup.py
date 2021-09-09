# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 19:30:02 2021

@author: zhill
"""
import os
from distutils.core import setup
import py2exe
import sys

Mydata_files = []
for files in os.listdir('C:/Users/zhill/OneDrive/CrashCourse/Part II/alien_invasion/images/'):
    f1 = 'C:/Users/zhill/OneDrive/CrashCourse/Part II/alien_invasion/images/' + files
    if os.path.isfile(f1): # skip directories
        f2 = 'images', [f1]
        Mydata_files.append(f2)

setup(
      console = [{
          'script': 'alien_invasion.py',
          'icon_resources': [(0,'images/alien_cd.ico')]}],
      data_files = Mydata_files,
      options = {
          "py2exe":{
              "excludes": ["_pytest","rewrite"]
                      } 
                  }
      )