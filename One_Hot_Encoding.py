"""
Created on Tue Oct 26 12:54:56 2021

@author: Danial Arab
"""
# Applying One-Hot Encoding through keras - to_categorical

from scipy.io import loadmat
from tensorflow.keras.utils import to_categorical

data = loadmat('ex3data1.mat')
X = data['X']
y = data['y']

y = to_categorical (y)
