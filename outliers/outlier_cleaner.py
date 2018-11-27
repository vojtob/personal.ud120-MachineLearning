#!/usr/bin/python

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    bannedData = []
    for removeCount in range(10):
        maxError = 0
        maxErrorIndex = -1
        # find the biggest errror
        for i in range(len(ages)):
            if i in bannedData:
                continue
            error = abs(predictions[i] - net_worths[i])
            if(error > maxError):
                maxError = error
                maxErrorIndex = i
        bannedData.append(maxErrorIndex)
           
    cleaned_data = []
    for i in range(len(ages)):
        if i in bannedData:
            continue
        error = abs(predictions[i] - net_worths[i])
        cleaned_data.append((ages[i], net_worths[i], error))

    return cleaned_data

