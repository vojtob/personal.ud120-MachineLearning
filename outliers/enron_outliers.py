#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

def checkBandit(data):
    if data["salary"] == "NaN":
        return False
    if data["bonus"] == "NaN":
        return False
    if int(data["salary"]) < 1000000:
        return False
    if int(data["bonus"]) < 5000000:
        return False
    return True
    

### read in data dictionary, convert to numpy array
#data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
with open("../final_project/final_project_dataset.pkl", "rb") as f1:
    data_dict = pickle.load(f1)

# clean data
data_dict.pop("TOTAL", 0)
for k in data_dict:
    data = data_dict[k]
    if(checkBandit(data)):
        print("name: {0:20} salary: {1:12} bonus: {2:12}".format(k, data["salary"], data["bonus"]))

features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )
#    if((salary > 1000000) and (:
#        print("outlier: ", point)

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


