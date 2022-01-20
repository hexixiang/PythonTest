import tensorflow as tf
import numpy as np
import os
import cv2

from tensorflow.keras.models import Sequential
from tensorflow.keras import layers
from sklearn import metrics, neighbors
from tensorflow import keras
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, roc_curve
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import time
from sklearn.ensemble import RandomForestClassifier

list_y = ['WWW','MAIL','FTP-CONTROL','FTP-PASV','ATTACK','P2P','DATABASE','FTP-DATA','MULTIMEDIA','SERVICES','INTERACTIVE','GAMES']
#read the file,change 'Y,N,?,', 转换为0，1;y,n在77，78，79，80，83，84
def data_prepross(filename):
    X, Y = [], []
    for f in filename:
        print(f)
        with open(os.getcwd() + '/' + f, 'r') as file:

            for n, i in enumerate(file.readlines()[253:]):#从253行开始读入数据
                i = i.replace('Y','1')
                i = i.replace('N', '0')
                spl = i.split(',')
                if spl.count('?')>8:
                    continue
                i = i.replace('\n', '')
                fz = [float(f) for f in i.split(',')[:-1] if f != '?']
                meana = sum(fz) / len(fz)
                i = i.replace('?', str(0))
                #均值填充，加高斯白噪声
                #x = [float(j) for j in i.split(',')[:-1]] +[meana]*8  +  np.random.normal(0,1,256)
                x = [float(j) for j in i.split(',')[:-1]] + [0] * 8
                #前期把N，Y变成0，1了，于是恢复过来
                y = i.split(',')[-1].replace('FTP-CO0TROL','FTP-CONTROL')
                y = y.replace('I0TERACTIVE','INTERACTIVE' )
                y = list_y.index(y)#标签值
                X.append(x)
                Y.append(y)
            file.close()
    return X, Y




#data nomalization
total_x,total_y = data_prepross(['entry01.weka.allclass.arff','entry02.weka.allclass.arff'])
for i in range(10):
    i1=np.array(total_x[i])
    i_image=i1.reshape(16,16)
    cv2.imwrite(str(i)+'.png',i_image)