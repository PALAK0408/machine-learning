# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle
load_model = pickle.load(open('C:/Users/HP/Downloads/trained_model.sav', 'rb'))

data = (70	,1,	2,	156,	245,	0,	2,	143,	0,	0,	1,	0,	3)

data_numpy = np.asarray(data)
data_reshape = data_numpy.reshape(1, -1)

prediction = load_model.predict(data_reshape)
print(prediction)

if (prediction[0] ==0):
  print("person does not have heart disease")

else:
  print("person have heart disease")
