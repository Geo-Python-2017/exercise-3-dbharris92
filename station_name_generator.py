# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 17:44:53 2018

@author: harrisab2
"""

###variables
basename = "Station"
filenames = []


###iterate over number rance 0-20
for number in range(21):
      ###create a variable to add onto interated #s
      station = basename + '_' + str(number) + '.txt'
      ###append to list
      filenames.append(station)  
print(filenames)