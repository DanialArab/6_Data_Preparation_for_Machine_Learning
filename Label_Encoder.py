"""
Created on Tue Oct 26 14:08:40 2021

@author: Danial Arab
"""
import numpy as np
from tensorflow.keras.utils import to_categorical


population = np.array([4641054775,  1340598147, 747636026, 
                       592072212, 430759766, 43111704])


continent = np.array(['Asia', 'Africa', 'Europe' , 'North America', 
                      'South America', 'Australia/Oceania'])

X = population;
y = to_categorical (continent)

from sklearn.preprocessing import LabelEncoder  
label_encoder = LabelEncoder() 

vector = label_encoder.fit_transform(continent) #create a vector

#Convert to categorical
y = to_categorical(vector)
