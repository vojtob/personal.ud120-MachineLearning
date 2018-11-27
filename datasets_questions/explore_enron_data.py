#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

with open("../final_project/final_project_dataset.pkl", "rb") as eDataFH:
    enron_data = pickle.load(eDataFH)

#print keys
#print(len(enron_data))
#for k in enron_data:
#    item = enron_data[k]
#    print(k)

#count = 0
#for k in enron_data:
#    item = enron_data[k]
#    if item["poi"] == 1:
#        count += 1
#print(count)

# features of person
#item = enron_data["PRENTICE JAMES"]
#for k in item:
#    print(k)

#print(enron_data["PRENTICE JAMES"]["total_stock_value"])
#print(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])
#print(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])
    
#max_salary = 0
#for k in enron_data:
#    item = enron_data[k]
##    print(item["salary"])
#    if(item["salary"] != "NaN"):
#        if int(item["salary"]) > max_salary:
#            max_salary = int(item["salary"])
#print(max_salary)        

noSalary = 0
noEmail = 0
count = 0
countPay = 0
for k in enron_data:
    item = enron_data[k]
#    if item["poi"]:
    count+=1
    if(item["total_payments"] != "NaN"):
        countPay += 1
    
print("total: {0}, no payments: {1}, % {2:.4f}".format(count, countPay, countPay/count))
