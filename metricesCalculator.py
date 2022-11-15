import os
from collections import Counter

import numpy as np
import pandas as pd
import tensorflow as tf
from bltk.langtools import Tokenizer as blT
from bltk.langtools.banglachars import (vowels,
                                        vowel_signs,
                                        consonants,
                                        digits,
                                        others)
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
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


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(tndset['wrong'], tndset['correct'], test_size=0.1)

# print("X_train Length: " , len(X_train))
print("X_train" , X_train)
# print("New Line")
# print()
#
# print("X_test Length: " , len(X_test))
# print("X_test" , X_test)
# print("New Line")
# print()
#
# print("y_train Length: " , len(y_train))
# print("y_train" , y_train)
# print("New Line")
# print()
#
# print("y_test Length: " , len(y_test))
# print("y_test" , y_test)



print("new set")
print(new_tdnset)