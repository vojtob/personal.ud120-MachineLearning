#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""

from tools.email_preprocess import preprocess

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
print("features_train:", features_train.shape)
print("features_test:", features_train.shape)
print("labels_train:", features_train.shape)
print("labels_test:", features_train.shape)

#########################################################
### your code goes here ###
from sklearn.naive_bayes import GaussianNB

clf = GaussianNB()
clf.fit(features_train, labels_train)
print("accuracy : {:.3}".format(clf.score(features_test, labels_test)))

#########################################################