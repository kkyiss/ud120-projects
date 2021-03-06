#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from time import time
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary
clf = KNeighborsClassifier(n_neighbors=4)
t0 = time()
clf = clf.fit(features_train,labels_train)
t1 = time()
pred = clf.predict(features_test)
t2 = time()
accuracy = accuracy_score(pred,labels_test)
print "KNN accuracy: %r" % (accuracy)
print "KNN training time: %r" % (round(t1-t0,3))
print "KNN predict time: %r" % (round(t2-t1,3))

clf = AdaBoostClassifier()
t0 = time()
clf = clf.fit(features_train,labels_train)
t1 = time()
pred = clf.predict(features_test)
t2 = time()
accuracy = accuracy_score(pred,labels_test)
print "Adaboost accuracy: %r" % (accuracy)
print "Adaboost training time: %r" % (round(t1-t0,3))
print "Adaboost predict time: %r" % (round(t2-t1,3))

clf = RandomForestClassifier()
t0 = time()
clf = clf.fit(features_train,labels_train)
t1 = time()
pred = clf.predict(features_test)
t2 = time()
accuracy = accuracy_score(pred,labels_test)
print "RandomForset accuracy: %r" % (accuracy)
print "RandomForset training time: %r" % (round(t1-t0,3))
print "RandomForset predict time: %r" % (round(t2-t1,3))

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
