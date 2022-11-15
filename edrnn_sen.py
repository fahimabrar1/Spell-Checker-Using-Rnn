# -*- coding: utf-8 -*-
"""EDRNN_Sen.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IDdp3gMmlK5huXI-SZO9I-7IKsI_R7fG
"""

# !pip install bltk

import tensorflow as tf
import pandas as pd
import numpy as np
from tensorflow import keras
from keras.preprocessing.text import Tokenizer
from bltk.langtools import Tokenizer as blT
from bltk.langtools.banglachars import (vowels,
                                        vowel_signs,
                                        consonants,
                                        digits,
                                        operators,
                                        punctuations,
                                        others)
from collections import Counter

# from google.colab import drive
# drive.mount('/content/drive')

nukta = u'\u09bc'

tndset_c = pd.read_csv('E:\Programming\Python\SP\Data\_final_wr_word_corpus_1h.csv')
tndset_c = tndset_c.dropna()
print(tndset_c)

# wdf = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/final_all_words_corpus.csv')
# words = list(wdf['words'])

# tndset = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/tndset_sen - Sheet1.csv')
tndset = pd.read_csv('E:\Programming\Python\SP\Data\_final_wr_sentence_corpus_1h.csv')
tndset = tndset.dropna()
print(tndset)

starter = "<start>"
ender = "<end>"


def read_corpus(corpus):
    fc = []
    tokenizer = blT()
    words = []
    for i, sen in enumerate(corpus['correct']):
        word = tokenizer.word_tokenizer(sen)
        for j in word:
            print("j", j)
            words.append(j)
    for i, sen in enumerate(corpus['wrong']):
        word = tokenizer.word_tokenizer(sen)
        for j in word:
            print("j", j)
            words.append(j)
    return words


words = read_corpus(tndset)

# allw_df = pd.DataFrame(words, columns=["words"]) 
# allw_df = allw_df.reset_index(drop=True)
# allw_df.to_csv('/content/drive/MyDrive/Colab Notebooks/final_all_words_corpus.csv')

len(words)

vocabs = set(words)
vocabs

len(vocabs)

word_counts = Counter(words)
word_counts

wordVocav = []
wordVocav.append(starter)
wordVocav.append(ender)
for i in vocabs:
    wordVocav.append(i)

print("Word Vocab Length: " + str(len(wordVocav)))
print(wordVocav)
print(len(wordVocav))

charVocab = []
charVocab.append(nukta)
for i in vowels:
    charVocab.append(i)

for i in vowel_signs:
    charVocab.append(i)

for i in consonants:
    charVocab.append(i)

for i in digits:
    charVocab.append(i)

for i in range(0, 5):
    charVocab.append(others[i])
print("Char Vocab Length: " + str(len(charVocab)))
print(charVocab)
print(len(charVocab))

w_vocabdict = dict(zip(wordVocav, range(0, len(wordVocav))))
w_vocabdict

rw_vocabdict = dict(zip(range(0, len(wordVocav)), wordVocav))
rw_vocabdict

c_vocabdict = dict(zip(charVocab, range(1, len(charVocab) + 1)))
c_vocabdict

rc_vocabdict = dict(zip(range(1, len(charVocab) + 1), charVocab))
rc_vocabdict

tX = tndset
tX

tX = tX.reset_index(drop=True)

tX_c = tndset_c
tX_c

c_newdf = tX_c
c_newdf

cnt = 0
for i in c_newdf['wrong']:
    if type(i) == float:
        cnt += 1
        print(i)
print(cnt)

w_newdf = tX
w_newdf

t_steps = 0
for i in w_newdf['wrong']:
    word_list = i.split()
    if t_steps < len(word_list):
        t_steps = len(word_list) + 1
print(t_steps)

maxlen = max(c_newdf['wrong'].values, key=len)
c_t_steps = len(maxlen) + 1
print(c_t_steps)

from keras import layers
from numpy import argmax
from numpy import array

for i in range(0):
    print(i)


def one_hot_encode_char(sequence, n_unique):
    encoding = []
    emp = []
    count = 0
    for i, letter in enumerate(sequence):
        vector = [0 for _ in range(n_unique)]
        # print(c_vocabdict[letter])
        vector[c_vocabdict[letter]] = 1
        encoding.append(vector)
        count += 1
    for i in range(c_t_steps - (count)):
        vector = [0 for _ in range(n_unique)]
        vector[0] = 1
        emp.append(vector)
    encoding = emp + encoding
    x = array(encoding)
    x = x.reshape((1, x.shape[0], x.shape[1]))
    return x


# one hot encode sequence
def one_hot_encode(sequence, n_unique):
    encoding = []
    emp = []
    count = 0
    w = sequence.split()
    for i, letter in enumerate(w):
        vector = [0 for _ in range(n_unique)]
        print(w_vocabdict[letter])
        vector[w_vocabdict[letter]] = 1
        encoding.append(vector)
        count += 1
    for i in range(t_steps - (count)):
        vector = [0 for _ in range(n_unique)]
        vector[0] = 1
        emp.append(vector)
    encoding = emp + encoding
    # print(sequence)
    # print(w)
    # print(encoding)
    x = array(encoding)
    x = x.reshape((1, x.shape[0], x.shape[1]))
    return x


# decode a one hot encoded string
def one_hot_decode(encoded_seq):
    ls = []
    for vector in encoded_seq:
        ls.append(argmax(vector))
    return ls


# arrX = []
# arrY = []
count = 0

trainX = [one_hot_encode(i[0], len(wordVocav)) for i in tX.values]
trainY = [one_hot_encode(i[1], len(wordVocav)) for i in tX.values]

trainY[0]

count = 0

for i, c in enumerate(trainX):
    if len(c[0]) > 10:
        count += 1
print(count)

count = 0
for i in trainX:
    if len(i[0]) > 10:
        count += 1

print(count)

count = 0
for i in trainY:
    if len(i[0]) > 15:
        count += 1

print(count)

# arrX = [[i[0]] for i in arrX]
# arrY = [[i[0]] for i in arrY]

# print(len(arrX))
# print(len(arrY))

# for i in arrY:
#     if len(i[0]) < 15:
#         print(i)
#         print(len(i))
#
# for i in arrX:
#     if len(i[0]) < 15:
#         print(len(i))

count = 0
lsX = list()
for i in trainX:
    lsX.append(i)

lsY = list()
for i in trainY:
    lsY.append(i)

# trainX = np.array(lsX)
# trainX[1].shape

# trainY = np.array(lsY)
# trainY[1].shape

# arrX = np.array(arrX).squeeze()
# arrY = np.array(arrY).squeeze()

# trainX = [[i] for i in trainX]
# trainY = [[i] for i in arrY]

print(len(wordVocav))

trainY = np.array(trainY)
trainY.shape

trainX = np.array(trainX)

trainY[:2]

# trainX = np.asarray(trainX)
# trainY = np.asarray(trainY)

print(trainX.shape)
print(trainY.shape)

type(trainX)

# trainX = trainX.reshape((1,trainX.shape[0],trainX.shape[1]))
# trainY = trainY.reshape((1,trainY.shape[0],trainY.shape[1]))

# arrX = np.array(arrX).squeeze()
# arrY = np.array(arrY).squeeze()

trainX = np.array(trainX).squeeze()
trainY = np.array(trainY).squeeze()

# print(arrX[:2])
#
# print(arrX[0])

print(trainX[0])

# # w = 'আমরা বাতে চাই'
# print(len(w))
# hotcode = one_hot_encode(w, len(wordVocav))
# nump = np.array(hotcode)
# nump.reshape(1, nump.shape[1], nump.shape[2])
# print(nump.shape)
# for i in nump:
#     print(i)
# hotdecode = one_hot_decode(hotcode[0])
# print(hotdecode)
# # print(hotcode[0][0])
#
# w = 'আমরা বাতে চাই'
# print(len(w))
# hotcode = one_hot_encode(w, len(wordVocav))
#
# print(hotcode)
# print("Squeezed:\n ")
#
# hotcode = np.array(hotcode).squeeze()
# print(hotcode)
#
# hotdecode = one_hot_decode(hotcode)
# print(hotdecode)
#
# testls = []
# for i in hotdecode:
#     if (i != 0):
#         testls.append(rw_vocabdict[i])
# print(testls)
#

numberofLSTMUnits = 256  # @param {type:"integer"}
batch_size = 32  # @param {type:"integer"}
n_features = len(wordVocav)

batch_size = 1

from keras.layers import Lambda
from keras import backend as K

test_input_data = np.zeros((batch_size, 1, n_features))
print(test_input_data[0])
test_input_data[:, 0, 0] = 1
print(test_input_data[0])
print(test_input_data)

print(trainX.shape)
print(trainY.shape)

# newX = trainX[:5000]
# newY = trainY[:5000]

newX = trainX
newY = trainY

encoder_inputs = tf.keras.layers.Input(shape=(t_steps, n_features), name='encoder_inputs')

# encoder_lstm1 = layers.LSTM(numberofLSTMUnits, return_state=True,  name='encoder_lstm')
# encoder_outputs1, state_h1, state_c1 = encoder_lstm(encoder_inputs)
# states1 = [state_h1, state_c1]

encoder_lstm = tf.keras.layers.LSTM(numberofLSTMUnits, return_state=True, name='encoder_lstm1')
encoder_outputs, state_h, state_c = encoder_lstm(encoder_inputs)

# initial context vector is the states of the encoder
states = [state_h, state_c]

# Set up the decoder layers
# Attention: decoder receives 1 token at a time &
# decoder outputs 1 token at a time 
decoder_inputs = tf.keras.layers.Input(shape=(1, n_features))
decoder_lstm = tf.keras.layers.LSTM(numberofLSTMUnits, return_sequences=True,
                                    return_state=True, name='decoder_lstm')
decoder_dense = tf.keras.layers.Dense(n_features, activation='softmax', name='decoder_dense')

all_outputs = []
# Prepare decoder initial input data: just contains the START character 0
# Note that we made it a constant one-hot-encoded in the model
# that is, [1 0 0 0 0 0 0 0 0 0] is the initial input for each loop
decoder_input_data = np.zeros((batch_size, 1, n_features))
decoder_input_data[:, 0, 0] = 1

# that is, [1 0 0 0 0 0 0 0 0 0] is the initial input for each loop
inputs = decoder_input_data
# decoder will only process one time step at a time
# loops for fixed number of time steps: n_timesteps_in
for _ in range(t_steps):
    # Run the decoder on one time step
    outputs, state_h, state_c = decoder_lstm(inputs,
                                             initial_state=states)
    outputs = decoder_dense(outputs)
    # Store the current prediction (we will concatenate all predictions later)
    all_outputs.append(outputs)
    # Reinject the outputs as inputs for the next loop iteration
    # as well as update the states
    inputs = outputs
    states = [state_h, state_c]

# Concatenate all predictions such as [batch_size, timesteps, features]
decoder_outputs = Lambda(lambda x: K.concatenate(x, axis=1))(all_outputs)

# Define and compile model 
model = tf.keras.Model(encoder_inputs, decoder_outputs, name='model_encoder_decoder')

# plot_model(model, show_shapes=True,show_layer_names=True)

model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

model.summary()

# arrX = np.asarray(arrX)
# arrY   = np.asarray(arrY)

len(lsX)

len(lsY)

print(trainX.shape)
print(trainY.shape)

print(newX.shape)
print(newY.shape)

from keras.callbacks import EarlyStopping

es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=5)

# model.fit(trainX,
#           trainY,
#           batch_size=batch_size,
#           epochs=50, 
#           callbacks=[es]
#           )


model.fit(newX,
          newY,
          batch_size=batch_size,
          epochs=1
          )
tf.saved_model.save(model, "E:/Programming/Python/SP/Model/edrnn_sen_1epoch")

# model.save("E:/Programming/Python/SP/Model/edrnn_sen_1epoch")
# import pickle
# filename = 'edrnn_sen_1epoch'
# pickle.dump(model, open(filename, 'wb'))

# newX[0]
#
# newY[0]
#
# aaa = newX[0]
# print(aaa.shape)
# aaa = aaa.reshape(1, aaa.shape[0], aaa.shape[1])
# print(aaa.shape)
#
# aaa = model.predict(aaa)
#
# """This is the Wrong Word From Dataset"""
#
# ls = [[argmax(i)] for i in newX[0]]
# testls = []
# for i in ls:
#     if i[0] != 0:
#         testls.append(rw_vocabdict[i[0]])
# print(testls)
# print("".join(testls))
#
# """This is the Right Word From Dataset"""
#
# ls = [[argmax(i)] for i in newY[0]]
# testls = []
# for i in ls:
#     if i[0] != 0:
#         testls.append(rw_vocabdict[i[0]])
# print(testls)
#
# """This is the prediction Of Wrong Word To Right"""
#
# ls = [[argmax(i)] for i in aaa[0]]
# regx = ''
# testls = []
# for i in ls:
#     if i[0] != 0:
#         testls.append(rw_vocabdict[i[0]])
# print(testls)
#
# p = " ".join(testls)
# print(p)
#
# len(newX)
#
# a = [one_hot_encode(i[0], len(wordVocav)) for i in tX.values]
# b = [one_hot_encode(i[1], len(wordVocav)) for i in tX.values]
# a = np.array(a)
# b = np.array(b)
#
# a.shape
# b.shape
#
# L = tX['wrong'].iloc[5]
# print(L)
#
# tX
#
# correctGuessCounter = 0
# correctToCount = len(newX)
# for j in range(len(newX)):
#     print(j)
#     wrong = a[j]
#     # wrong = wrong.reshape(1,wrong.shape[0],wrong.shape[1])
#     # right = right.reshape(1,right.shape[0],right.shape[1])
#     # print("Shape:")
#     # print(wrong.shape)
#     pred_Wrong = model.predict(wrong)
#     ls = [[argmax(i)] for i in pred_Wrong[0]]
#     testls = []
#     for i in ls:
#         if i[0] != 0:
#             testls.append(rw_vocabdict[i[0]])
#     # print(testls)
#
#     p = " ".join(testls)
#     print("wrong Word:", end='')
#     L = tX.iloc[j]['wrong']
#
#     print(L, end="\n")
#
#     print("Predicted Word:", end='')
#     print(p, end="\n")
#
#     print("Correct Word:", end='')
#     L = tX.iloc[j]['correct']
#     print(L, end="\n")
#
#     if p == L:
#         correctGuessCounter += 1
#         print("L")
# print("Accuracy:" + str(correctGuessCounter))
# print("Accuracy: {0}", str((correctGuessCounter / correctToCount)))
