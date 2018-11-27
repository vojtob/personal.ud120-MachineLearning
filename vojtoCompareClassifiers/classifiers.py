from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def getNB(features_train, labels_train):
    clf = GaussianNB()
    clf.fit(features_train, labels_train)
    return clf

def getSVM(features_train, labels_train):
    # clf = SVC(kernel="linear")
    clf = SVC(C=10)
    clf.fit(features_train, labels_train)
    return clf

def getTree(features_train, labels_train):
    clf = DecisionTreeClassifier(min_samples_split=2)
    clf.fit(features_train, labels_train)
    return clf

# def getAccuracy(clf, features_test, labels_test):
#     """ compute the accuracy of classifier """
#     return clf.score(features_test, labels_test)

def getAccuracy(clf, features_test, labels_test):
    """ compute the accuracy of classifier """
    pred = predict(clf, features_test)
    return accuracy_score(labels_test, pred)

def predict(clf, features_test):
    return clf.predict(features_test)