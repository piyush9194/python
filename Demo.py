
# List of tuples
listofTuples = [[57,'Piyush'],[78,"Aadi"],[50,'Piyush'],[78,"Aadi"]]

# Convert a list of tuple to dictionary
temDict = {item[1]: item[0] for item in listofTuples}

temDict = {}
for item in listofTuples:
    print(item)
    key,value = item[1],item[0]
    if key in temDict:
        temDict[key]+= value
    else:
        temDict[key] = value



print(temDict)