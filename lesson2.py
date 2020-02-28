#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 17:24:33 2020

@author: shirzlotnik
"""

import numpy as np
import tensorflow as tf
tf.logging.set_verbosity(tf.logging.ERROR)

tmp_c = np.array([-40,-10,0,8,15,22,38], dtype=float)
tmp_f = np.array([-40,14,32,46,59,72,100],dtype=float)

for i,c in enumerate(tmp_c):
    print("{} Celsius -> {} Fahrenhet".format(c,tmp_f[i]))
"""    
lay = tf.keras.layers.Dense(units=1,input_shape=[1])
model = tf.keras.Sequential([lay])
model.compile(loss='mean_squared_error',optimizer=tf.keras.optimizers.Adam(0.1))
history = model.fit(tmp_c,tmp_f,epochs=500,verbose=False)
print('finish  training')


import matplotlib.pyplot as plt
plt.xlabel('Epoch Number')
plt.ylabel("Loss Magnitude")
plt.plot(history.history['loss'])

#print(" 100 C is {} F ".format(model.predict([100.0])))
#print("these are the layers variables {}".format(lay.get_weights()))

lay1 = tf.keras.layers.Dense(units=4,input_shape=[1])
lay2 = tf.keras.layers.Dense(units=4)
lay3 = tf.keras.layers.Dense(units=1)

model = tf.keras.Sequential([lay1,lay2,lay3])
model.compile(loss='mean_squared_error',optimizer=tf.keras.optimizers.Adam(0.1))
history = model.fit(tmp_c,tmp_f,epochs=500,verbose=False)
print('finish  training!')
print(" 100 C is {} F ".format(model.predict([100.0])))
print("these are the layers variables {}".format(lay1.get_weights()))
print("these are the layers variables {}".format(lay2.get_weights()))
print("these are the layers variables {}".format(lay3.get_weights()))
"""

hidden = keras.layers.Dense(units=2,input_shape=[3])
output = keras.layers.Dense(units=1)
model = tf.keras.Sequential([hidden,output])