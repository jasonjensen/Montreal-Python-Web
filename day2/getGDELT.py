# Copyright 2014, Radhika S. Saksena (radhika dot saksena at gmail dot com)
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Web scraping and text processing with Python workshop

import urllib2
import sys
import os
import time

'''Download the full resolution GDELT event dataset for March 2014.'''

month = 3

# make a gdelt/ directory if it doesn't already exist
if not os.path.exists(os.getcwd() + "/gdelt"):
    os.mkdir(os.getcwd() + "/gdelt")

# try downloading the files comprising events data for March 2014
#for day in range(1,31):
for day in range(1,7):

    # construct the URL from which we retrieve the (compressed) events files
    fileName = "2014%02d%02d.export.CSV.zip" % (month,day)
    fileURL = "http://data.gdeltproject.org/events/%s"  % (fileName)
    localFile = os.getcwd() + "/gdelt/" + fileName

    print("Downloading file " + fileURL + " ...")

    # use the urllib2 module to fetch the events data file
    resp = urllib2.urlopen(fileURL)

    # write the retrieved events file to a local file
    with open(localFile,"wb") as fout:
        fout.write(resp.read())

    print("Downloaded file %s." % fileURL)

    # inject delay between consecutive fetches
    time.sleep(5)
