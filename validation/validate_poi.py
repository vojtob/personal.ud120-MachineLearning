#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle

from sklearn.tree import DecisionTreeClassifier
from sklearn import model_selection
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score

from tools.feature_format import featureFormat, targetFeatureSplit

with open("final_project/final_project_dataset.pkl", "rb") as fData:
    data_dict = pickle.load(fData)

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.

features_list = ["poi", "salary"]
#data = featureFormat(data_dict, features_list, sort_keys = 'tools/python2_lesson13_keys.pkl')
data = featureFormat(data_dict, features_list, sort_keys = 'tools/python2_lesson14_keys.pkl')
labels, features = targetFeatureSplit(data)
train_features, test_features, train_labels, test_labels = model_selection.train_test_split(features, labels, test_size=0.3, random_state=42)

print("test size", len(test_labels))
print(test_labels)

### it's all yours from here forward!  
clf = DecisionTreeClassifier()
clf.fit(train_features, train_labels)
pred = clf.predict(test_features)
#pred2 = 29 * [0.0]
#print("accuracy: {:.3f}".format(clf.score(test_features, test_labels)))
print("accuracy: {:.3f}".format(accuracy_score(test_labels, pred)))
#print("accuracy2: {:.3f}".format(accuracy_score(test_labels, pred2)))
print(classification_report(test_labels, pred, target_names=["NO", "YES"]))
print(confusion_matrix(test_labels, pred))
print("precision: : {:.3f}  recall: {:.3f}".format(
        precision_score(test_labels, pred), 
        recall_score(test_labels, pred)))

print("DONE")

