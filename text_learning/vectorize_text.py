#!/usr/bin/python

import pickle

from vojtoUtils.perf import PerformanceTimer

from sklearn.feature_selection import SelectPercentile, f_classif
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import model_selection
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier



"""
    Starter code to process the emails from Sara and Chris to extract
    the features and get the documents ready for classification.

    The list of all the emails from Sara are in the from_sara list
    likewise for emails from Chris (from_chris)

    The actual documents are in the Enron email dataset, which
    you downloaded/unpacked in Part 0 of the first mini-project. If you have
    not obtained the Enron email corpus, run startup.py in the tools folder.

    The data is stored in lists and packed away in pickle files at the end.
"""
        
def prepareData():
    t = PerformanceTimer("Preparing data")
    
    # read emails
    t.startTimer("read email")
    with open("vojto_email_data.pkl", "rb") as fWord:
        emails = pickle.load(fWord)
    with open("vojto_email_authors.pkl", "rb") as fAuhtors:
        authors = pickle.load(fAuhtors)        
#    email_data, from_data = readEmails()
    print("emails read:", len(emails))
    t.stopTimer()

    # split train and test
    t.startTimer("split")
    train_emails, test_emails, train_authors, test_authors = model_selection.train_test_split(emails, authors, test_size=0.1, random_state=42)
    t.stopTimer()
    print("train mails size:", len(train_emails))
    print("test mails size:", len(test_emails))
    
    ### TfIdf vectorization
    t.startTimer("data vectorized")
    v = TfidfVectorizer(stop_words="english")
    train_emails = v.fit_transform(train_emails)
    test_emails = v.transform(test_emails)
    t.stopTimer()
    print("number of words:", len(v.get_feature_names()))
    print("processedEmailsTrain shape:", train_emails.shape)
    print("processedEmailsTest shape:", test_emails.shape)

    # dimension reduction
#    t.startTimer("reduced dimension")
#    selector = SelectPercentile(f_classif, percentile=1)
#    selector.fit(train_emails, train_authors)
#    train_emails = selector.transform(train_emails).toarray()
#    test_emails  = selector.transform(test_emails).toarray()
#    t.stopTimer()
#    print("reducedEmailsTrain shape:", train_emails.shape)
#    print("reducedEmailsTest shape:", test_emails.shape)
    
    t.printTimers()
    
    return train_emails, train_authors, test_emails, test_authors

def testClassifier(algName, clf, features_train, labels_train, features_test, labels_test):
    t.startTimer(algName)
    clf.fit(features_train, labels_train)
    results.append((algName, clf.score(features_test, labels_test)))
    t.stopTimer()
    print(algName + " tested")


## prepare data
emailTrain, authorTrain, emailTest, authorTest = prepareData()

## process 
t = PerformanceTimer("classifiers")
results = []

# NB
#testClassifier("Naive Bayes", GaussianNB(), emailTrain, authorTrain, emailTest, authorTest)
# SVM
#testClassifier("SVM", SVC(C=10), emailTrain, authorTrain, emailTest, authorTest)
# Tree classifier
emailTrain = emailTrain[:150].toarray()
authorTrain   = authorTrain[:150]
#testClassifier("Decision Tree", DecisionTreeClassifier(min_samples_split=2), emailTrain, authorTrain, emailTest, authorTest)
clf = DecisionTreeClassifier(min_samples_split=2)
clf.fit(emailTrain, authorTrain)
results.append(("TREE", clf.score(emailTest, authorTest)))
vMax = 0
iMax = 0
c = 0
for i in range(len(clf.feature_importances_)):
    x = clf.feature_importances_[i]
    if x > vMax:
        vMax = x
        iMax = i
    if x > 0.2:
        c += 1
print("max", vMax)
print("index", iMax)
print("count", c)

# k neighbour
#for i in range(2,11):
#    testClassifier("KNeighborsClassifier" + str(i), KNeighborsClassifier(n_neighbors=i), emailTrain, authorTrain, emailTest, authorTest)
# random forest
#for i in range(5,120,5):
#    testClassifier("randomForest" + str(i), RandomForestClassifier(n_estimators=i), emailTrain, authorTrain, emailTest, authorTest)
# ada boost
#for i in range(5,80,5):
#    testClassifier("adaboost" + str(i), AdaBoostClassifier(n_estimators=i), emailTrain, authorTrain, emailTest, authorTest)


print()
print("{:20} {:>10}".format("Algorithm", "Accuracy"))
for r in results:
    print("{:20} {:10.3}".format(r[0], r[1]))

print()
t.printTimers()

