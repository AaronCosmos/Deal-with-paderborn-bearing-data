#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: Aaron Liu time:2019/3/28

from scipy.io import loadmat
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

#Loadmat For Example
mat_dict=loadmat("N09_M07_F10_KI14_1.mat")
#Get the viberation signal location,you can choose current signal with other numbers
file=mat_dict['N09_M07_F10_KI14_1']['Y'][0][0][0][6][2]
Vb_sig=file[2]
Vb_sig=pd.DataFrame(Vb_sig)
Vb_sig2=Vb_sig.T
