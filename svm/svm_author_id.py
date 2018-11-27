#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
from tools.email_preprocess import preprocess
from time import perf_counter

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
print("start preprocess")
s = perf_counter();
features_train, features_test, labels_train, labels_test = preprocess()
print("end preprocess in ", perf_counter()-s)

for i in range(20):
    print(labels_train[i], features_train[i])


# from sklearn.svm import SVC

# # clf = SVC(kernel="linear")
# # print("{:>10} {:>7} {:>8}".format("C", "%", "time"))
# # Cs = [1,10,100,1000,10000]
# # for C in Cs:  
# #     clf = SVC(kernel="rbf", C=C)
# #     clf.fit(features_train[:len(features_train)//100], labels_train[:len(labels_train)//100])
# #     # clf.fit(features_train, labels_train)
# #     elapsedTime = perf_counter()-s
# #     print("{:>10} {:7.2%} {:>6.1f}".format(C, clf.score(features_test, labels_test), elapsedTime))

# t = []
# clf = SVC(kernel="rbf", C=10000)
# t.append(perf_counter())
# clf.fit(features_train, labels_train)
# t.append(perf_counter())
# pred = clf.predict(features_test)
# t.append(perf_counter())

# counter = 0
# for d in pred:
#     if d == 1:
#         counter += 1
# print(counter)

# for i in range(1, len(t)):
#     print("elapsed time:", t[i]-t[i-1])
