#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1

    sklearn version 0.20
    numpy version 1.15
"""
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.naive_bayes import GaussianNB

# use Naive Bayes alg.
clf = GaussianNB()
t0 = time()

# model train
clf.fit(features_train, labels_train)
t1 = time()

# model predict
pre = clf.predict(features_test)
t2 = time()

print "training time:", round(t1-t0,3), "s"
print "predict time:", round(t2-t1,3), "s"

from sklearn.metrics import accuracy_score

# model accuracy
accuracy = accuracy_score(pre,labels_test)
print accuracy
#########################################################

