# -*- coding: utf-8 -*-
"""
Created on Mon Mar 05 15:38:44 2018

@author: ankur
"""

import pandas as pd
import glob
import os
path=r'C:\Imagine\P'

allf=glob.glob(path + '\*')

for i in range(0,len(allf)):
    folder=allf[i]
    name=os.path.basename(folder)
    for filename in os.listdir(folder):
        os.rename(folder+'\\'+ filename, folder+'\\'+ name+'_'+filename)
    