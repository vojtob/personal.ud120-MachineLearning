#!/usr/bin/python

import pickle

from vojtoUtils.perf import PerformanceTimer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier



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
        
## prepare data
t = PerformanceTimer("classifiers")

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

train_emails = train_emails[:150].toarray()
train_authors   = train_authors[:150]
#testClassifier("Decision Tree", DecisionTreeClassifier(min_samples_split=2), emailTrain, authorTrain, emailTest, authorTest)
clf = DecisionTreeClassifier(min_samples_split=2)
clf.fit(train_emails, train_authors)
print("TREE accuracy", clf.score(test_emails, test_authors))

t.startTimer("find max")
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
        print("high word:", i, x)
print("max", vMax)
print("index", iMax)
print("count", c)
t.stopTimer()
print(v.get_feature_names()[iMax])

print()
t.printTimers()

