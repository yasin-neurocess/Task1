# Interview for Software Engineer position of Neurocess Inc. in July 2022 : Task1
# Candidate: Yasin Ozdemir - tr.yasinozdemir@gmail.com

# I'm sure code's working when I uploaded on Github the latest...
# ...if you have problems about code, please feel free to contact me..

# thank you for giving me the opportunity to be a part of Neurocess Inc.

import pickle
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read the 'data.pkl' file as dataframe
dFrame = pd.read_pickle('data.pkl')
# log
print(dFrame)

# size of dataframe
dfSize = len(dFrame)
# log
print(dfSize)

# read the 'names.json' file as nFrame
with open('names.json', 'r') as f:
    nFrame = json.load(f)
# log
print(nFrame)

# size of namesframe
nfSize = len(nFrame)
# log
print(nfSize)

namesCounter = 1
j = 0
valueCounter = 0

# create arrays for bar plot
updatedOnes = np.empty((nfSize), object)
counterOnes = np.zeros((nfSize), int)

# evidence to theory of everything (:
for i in range(dfSize):
    if dFrame.loc[i, 'task'] == 1.0:
        nKey, nValue = list(nFrame.items())[j]
        nKey = int(nKey)
        if nKey == namesCounter:
            dFrame.loc[i, 'task'] = nValue
            # log
            print(i)
            print(dFrame.loc[i, 'task'])
            valueCounter += 1
            print(valueCounter)
            if dFrame.loc[i+1, 'task'] == 0:
                # log
                print(dFrame.loc[i+1, 'task'])
                namesCounter += 1
                # log
                print(namesCounter)
                print(nValue)
                print(valueCounter)
                # value assignments for the bar plot
                updatedOnes[j] = nValue
                counterOnes[j] = valueCounter
                j += 1
                # log
                print(j)
                valueCounter = 0
                # log
                print(updatedOnes)
                print(counterOnes)

# write updated data frame on a new file as 'new-data.pkl'
with open('new-data.pkl', 'wb') as handle:
    pickle.dump(dFrame, handle, protocol=pickle.HIGHEST_PROTOCOL)

# press the arrays on bar plot
y_pos = np.arange(len(updatedOnes))
plt.bar(y_pos, counterOnes, color="purple")
plt.xticks(y_pos, updatedOnes)
plt.xlabel("updatedOnes")
plt.ylabel("counterOnes")
plt.title("Task1 Solution")
plt.show()
