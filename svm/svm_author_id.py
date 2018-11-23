#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###


#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]

# use SVM classify
#clf = SVC(kernel='linear')
#clf = SVC(kernel='rbf')
clf = SVC(kernel='rbf', C=10000.)
t0 = time()

clf.fit(features_train,labels_train)
t1 = time()
pre = clf.predict(features_test)
t2 = time()

accuracy = accuracy_score(pre,labels_test)
print "SVM accuracy: %r" % (accuracy)

print "10th: %r, 26th: %r, 50th: %r" % (pre[10], pre[26], pre[50])
print "No. of predicted to be in the 'Chris'(1): %r" % sum(pre)


print "training time:", round(t1-t0,3), "s"
print "predict time:", round(t2-t1,3), "s"

#########################################################


