#!/usr/bin/python

""" Complete the code in ClassifyNB.py with the sklearn
    Naive Bayes classifier to classify the terrain data.

    The objective of this exercise is to recreate the decision
    boundary found in the lesson video, and make a plot that
    visually shows the decision boundary """

from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier

from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

from time import perf_counter

#import classifiers
#  import getNB, getSVM, getTree, getAccuracy

import numpy as np
import pylab as pl

features_train, labels_train, features_test, labels_test = makeTerrainData()

### the training data (features_train, labels_train) have both "fast" and "slow" points mixed
### in together--separate them so we can give them different colors in the scatterplot,
### and visually identify them
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii] == 0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii] == 0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii] == 1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii] == 1]

results = []
def addResult(algorithm, accuracy, time):
    results.append((algorithm, accuracy, time))
    
def testClassifier(clf, algName):
    s = perf_counter()
    clf.fit(features_train, labels_train)
#    prettyPicture(clf, features_test, labels_test, algName.strip() +".png")
    pred = clf.predict(features_test)
    acc = accuracy_score(labels_test, pred)
    s = perf_counter() - s
    addResult(algName, acc, s)

# NB classifier
testClassifier(GaussianNB(), "Naive Baise")

# SVM classifier
# clf = SVC(kernel="linear")
testClassifier(SVC(C=10), "SVM")

# Tree classifier
testClassifier(DecisionTreeClassifier(min_samples_split=2), "Decision Tree")

# k neighbour
for i in range(2,11):
    testClassifier(KNeighborsClassifier(n_neighbors=i), "KNeighborsClassifier" + str(i))

# random forest
for i in range(5,120,5):
    testClassifier(RandomForestClassifier(n_estimators=i), "randomForest" + str(i))

# random forest
for i in range(5,80,5):
    testClassifier(AdaBoostClassifier(n_estimators=i), "adaboost" + str(i))

# print results
print("{:20} {:>10} {:>10}".format("Algorithm", "Accuracy", "Time"))
for r in results:
    print("{:20} {:10.3f} {:10.2f}".format(r[0], r[1], r[2]))