# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 23:09:38 2020

"""

# This file is for PAMAP2 data processing
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import math
import h5py
import os
activityIDdict = {
              1: 'walking',
              2: 'walking_upstairs',
              3: 'walking_downstairs',
              4: 'sitting',
              5: 'standing',
              0: 'laying',# originally was 6
              }
colNames = ['body_acc_x','body_acc_y','body_acc_z',
            'body_gryo_x','body_gryo_y','body_gryo_z',
            'total_acc_x','total_acc_y','total_acc_z']  
            
def read_files():
    list_of_Xs = ['./test/Inertial Signals',
                     './train/Inertial Signals']
    
    list_of_ys = ['./test/y_test.txt',
                  './train/y_train.txt']
      

    
    # To merge the data from nine features, first convert each txt to numpy array, then dstack them
    train_X_array = []
    files = os.listdir(list_of_Xs[1])
    for file in files:
        print(file," is reading...")
        data = np.loadtxt(list_of_Xs[1]+'/'+file)
        #print("data shape is:", data.shape)
        train_X_array.append(data)
     
    # merge the test files
    test_X_array = []
    files = os.listdir(list_of_Xs[0])
    for file in files:
        print(file," is reading...")
        data = np.loadtxt(list_of_Xs[0]+'/'+file)
#        print("data shape is:", data.shape)
        test_X_array.append(data)
        
    train_X = np.dstack(train_X_array)
    print(train_X.shape)
    
    test_X = np.dstack(test_X_array)
    print(test_X.shape)
        
    train_y = np.loadtxt(list_of_ys[1])
    test_y = np.loadtxt(list_of_ys[0]) 
    print(train_y.shape)
    print(test_y.shape)
    
    # merge trainX and testX, the data will be split to train and test set during model training
    X = np.vstack((train_X, test_X)) 
    # merge train_y and test_y
    y = np.hstack((train_y,test_y)).astype(np.int) #convert to integer
    y = np.where(y==6,0,y) # if the label is 6, replace with 0, otherwise still y
   
    print("X shape is ", X.shape)
    print("y shape is ", y.shape)
    print(set(y))
    return [X,y]
    #return {'inputs' : X, 'labels': y}


def save_data(arr,file_name): # save the data in h5 format
    dict_ = {'inputs' : arr[0], 'labels': arr[1]}
    f = h5py.File(file_name,'w')
    for key in dict_:
        print(key)
        f.create_dataset(key,data = dict_[key])       
    f.close()
    print('Done.')    

#only plot a window
#Since the data has already processed into windows, and shuffled to test and train dataset.
#It is sequential within each window.
def window_plot(X, y, col, y_index):
    unit='ms^-2'
    #print(y.shape)
    #print(X.shape)
    x_seq = X[y_index][:,col]
    #print(x_seq.shape)
    #print(y[y_index])
    plottitle = colNames[col]+' - '+ activityIDdict[y[y_index]]
    plt.plot(x_seq)
    plt.title(plottitle)
    plt.xlabel('window')
    plt.ylabel(unit)
    plt.show()

if __name__ == "__main__":
    file_name = 'uci_har.h5'
    arr = read_files()
    #check the waves in a sigle window
    window_plot(arr[0],arr[1],2,500)
    save_data(arr,file_name)

    

    
    
