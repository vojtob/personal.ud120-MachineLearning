# -*- coding: utf-8 -*-
from time import perf_counter

class PerformanceTimer:
    results = {}
    timerName = None
    lastTimerName = None
    
    def __init__(self, timerName):
        self.timerName = timerName
        
    def startTimer(self, stepName=None):
        if stepName is None:
            stepName = self.timerName
        self.results[stepName] = perf_counter()
        self.lastTimerName = stepName
        
    def stopTimer(self, stepName=None):
        if stepName is None:
            stepName = self.lastTimerName
        if stepName in self.results:
            self.results[stepName] = perf_counter() - self.results[stepName]
    
    def getTime(self, stepName=None):
        if stepName is None:
            stepName = self.lastTimerName
        if stepName in self.results:
            return self.results[stepName]
    
    def printTimer(self, stepName=None):
        if stepName is None:
            stepName = self.lastTimerName
        if stepName in self.results:
            print("{:20} DONE in {:10.2f}s".format(stepName, self.results[stepName]))    
            
    def printTimers(self):
        print("{:20} {:>10}".format("Step", "Time"))
        for stepName, stepTime in self.results.items():
            print("{:20} {:10.2f}".format(stepName, stepTime))    
        