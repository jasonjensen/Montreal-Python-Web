# Copyright 2014, Radhika S. Saksena (radhika dot saksena at gmail dot com)
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Web scraping and text processing with Python workshop

import sys
import os
import time
import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import urllib2

warnings.filterwarnings('ignore')

'''Bar chart of event counts per country March 2014.'''

month = 3 # set month to March

# exit if gdelt/ directory if it doesn't already exist
if not os.path.exists(os.getcwd() + "/gdelt"):
    raise "Data directory does not exist."
    sys.exit(-1)

# get the column names for the GDELT dataset
headerURL = "http://gdeltproject.org/data/lookups/CSV.header.historical.txt"
headerStr = urllib2.urlopen(headerURL).read()
colNames = headerStr.split("\t")
#colNames = open("CSV.header.historical.txt","r").readline().split("\t")
colNames.append("SOURCEURL")

# initializee frequency table
allCnt = 0

#for day in range(1,31):
for day in range(1,7):
    # construct the URL from which we will try to retrieve the record
    fileName = "2014%02d%02d.export.CSV" % (month,day)
    localFile = os.getcwd() + "/gdelt/" + fileName

    # check if the dataset for this date exists
    if(not os.path.exists(localFile)):
        continue

    frame = pd.read_csv(localFile,sep="\t",names=colNames)

    # assign the event to a country if it's either one of the actors
    actor1Cnt = frame['Actor1CountryCode'].value_counts()
    actor2Cnt= frame['Actor2CountryCode'].value_counts()

    allCnt += actor1Cnt + actor2Cnt

# convert the frequency table in to a form suitable for plotting
allCnt = allCnt.order(ascending=True)

maxCountry,maxCount = max(allCnt.iteritems(),key=lambda x: x[1])
print("Maximum frequency encountered: " + str(maxCount))
print("Maximum frequency encountered for country: " + maxCountry)


# subset the frequency table to save only high frequency entries
allCnt = allCnt[allCnt > 0.05*maxCount]

# take the log of the frequencies
allCnt = np.log(allCnt)



# now plot the frequency table as a bar graph
plt.figure(figsize=(8,8))
pos = np.arange(len(allCnt.values))

plt.title('Frequency distribution of countries in the news database.')
plt.barh(pos,allCnt.values,color=["#006633"]*len(pos))

annotations = ["{0:4.2e}".format(np.exp(v)) for v in allCnt.values]
for p,c,val in zip(pos,annotations,allCnt.values):
    plt.annotate(str(c), xy=(val,p+.5),va='center')

ticks = plt.yticks(pos + .5,allCnt.keys())

plt.grid(axis='x',color='white',linestyle='-')

plt.show()
