# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 02:01:23 2022

@author: maham
"""

import os
import shutil 

dirName = input('Enter folder name:')

li = os.listdir(dirName)

for i in li:
    
    fileName,extension = os.path.splitext(i)
    
    extension =extension[1:]
    
    if  extension =='':
        
        continue
    
    if os.path.exists(dirName+'/'+extension):
        
        shutil.move(dirName+'/'+i,dirName+'/'+extension+'/'+i)
        
    else:
        
        os.makedirs(dirName+'/'+extension)
        
        shutil.move(dirName+'/'+i,dirName+'/'+extension+'/'+i)