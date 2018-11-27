# -*- coding: utf-8 -*-
import pickle
import os

from tools.parse_out_email_text import parseOutText
from vojtoUtils.perf import PerformanceTimer

def processMail(path):
    with open("../" + path) as email:
        processedText = parseOutText(email)
        for wordToRemove in ["sara", "shackleton", "sshacklensf", "chris", "germani", "cgermannsf"]:
            processedText = processedText.replace(wordToRemove, "")
    return processedText
    
def processAndStoreMails():
    from_data = []
    email_data = []
    
    # processing emails
    mailDef = [(0, "from_sara.txt"), (1, "from_chris.txt")]

    for personIndex, fileName in mailDef:
#        temp_counter = 0    
        with open("text_learning/" + fileName, "r") as f:
            for path in f:
                email = processMail(path.rstrip())
                email_data.append(email)
                from_data.append(personIndex)
#                if temp_counter == 100:
#                    break
#                temp_counter += 1     

    with open("vojto_email_data.pkl", "wb") as fWord:
        pickle.dump(email_data, fWord)
    with open("vojto_email_authors.pkl", "wb") as fAuhtors:
        pickle.dump(from_data, fAuhtors)
        
    print("emails processed")
    print("number of emails:", len(email_data))

#########
#########    
    
print("WD: ", os.getcwd())
t = PerformanceTimer("processing mails")
t.startTimer()
processAndStoreMails()
t.stopTimer()
t.printTimers()