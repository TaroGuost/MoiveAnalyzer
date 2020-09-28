# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.layers import Input , Dropout , Embedding , Concatenate, Dot , Dense  , Reshape , Flatten
from keras.models import Model
from keras.optimizers import Adam
import tensorflow as tf
import random as rd


def parse_people(people):
  result = 0.0
  if people[-1] == '万':
    result = float(people[:2])
    result = result *10000
  else:
    result = float(people)
  
  return result

data = pd.read_csv('temp.csv')

for i in range(len(data)):
  data.loc[i ,'people'] = parse_people(data.loc[i ,'people'])



moive_list = data.loc[: , 'title']

rating = pd.DataFrame(columns = ['userid' , 'title' , 'rating'])
count = 0


for i in range(10):
  for j in range(len(moive_list)):
    id = i
    rate = round(rd.uniform(0, 5), 2)
    if rate > 1.5:
      rating.loc[count] = [id] + [j] + [str(rate)]
      count +=1
    
'''
combine = rating.pivot_table(index=['userid'] , columns=['title'] , values = 'rating')

def pearson(s1 , s2):
  s1_c = s1 - s1.mean()
  s2_c = s2 - s2.mean()
  return np.sum(s1_c *s2_c) / np.sqrt(np.sum(s1_c**2)*np.sum(s2_c**2))

def find_moive(title , combine):
  max = 0.0
  result = ''
  titles = combine.columns
  for t in titles:
    if t != title:
      temp = pearson(combine[title] , combine[t])
      max = temp if temp > max else max 
      result = t if max == temp else result
      
      
  return result + ' is the best moive watch for next with value of ' + str(max)


find_moive('4x4' , combine)
'''

def embedding_input(name , n_in , n_out , reg):
  inp = Input(name = name , shape = [1])
  return inp , Embedding(name = name+'em' , input_dim = n_in , output_dim = n_out)(inp)

n_user = rating.userid.nunique()
n_movies = rating.title.nunique()  

user_in,u = embedding_input('user_in',n_user,50 , 1e-4)
moive_in , m = embedding_input('moive_in' ,n_movies , 50 , 1e-4)



x = Concatenate()([u,m])
x = Flatten()(x)
x = Dropout(0.3)(x)
x = Dense(70 , activation = 'relu')(x)
x = Dropout(0.75)(x)
x = Dense(1)(x)
nn = Model([user_in , moive_in] , x)
nn.compile(Adam(0.001) , loss='mse')

msk = np.random.rand(len(rating)) < 0.8
trn = rating[msk]
val = rating[~msk]

nn.fit([trn.userid , trn.title] , trn.rating , batch_size = 64 , epochs = 10
       , validation_data = ([val.userid , val.title], val.rating))


  



