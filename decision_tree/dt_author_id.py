#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
from tools.email_preprocess import preprocess
from time import perf_counter

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
print("start Tree")
s = perf_counter()
features_train, features_test, labels_train, labels_test = preprocess()
print("preprocess time: ", perf_counter()-s)

#########################################################
### your code goes here ###

print("data points count: ", len(features_train))
print("features count: ", len(features_test[0]))

s = perf_counter()
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(min_samples_split=40)
clf.fit(features_train, labels_train)
print("fit time: ", perf_counter()-s)

s = perf_counter()
print("accuracy : {:.3}".format(clf.score(features_test, labels_test)))
print("accuracy time: ", perf_counter()-s)
