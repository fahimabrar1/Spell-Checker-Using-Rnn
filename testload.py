import tensorflow as tf
import pandas as pd
import numpy as np
from tensorflow import keras
import pickle


filename = 'E:/Programming/Python/SP/Model/edrnn_sen_1epoch'

model = tf.saved_model.load(filename)
model.summary()
