# Copyright 2014, Radhika S. Saksena (radhika dot saksena at gmail dot com)
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Web scraping and text processing with Python workshop

import urllib2
import sys
import os
import time

'''Download "Entire Issue" of the Congressional Record for the period May 1 - 31 2014.'''

month = 5 # set month to May

# make an archive/ directory if it doesn't already exist
if not os.path.exists(os.getcwd() + "/archive"):
    os.mkdir(os.getcwd() + "/archive")

# try downloading the Congressional Record for May 2014
#for day in range(1,31):
for day in range(1,6):

    # construct the URL from which we will try to retrieve the record
    fileName = "CREC-2014-%02d-%02d.pdf" % (month,day)
    fileURL = "http://beta.congress.gov/crec/2014/%02d/%02d/%s"  % (month,day,fileName)
    localFile = os.getcwd() + "/archive/" + fileName

    try:
        # use the urllib2 module to fetch the record
        resp = urllib2.urlopen(fileURL)

        # write the record (PDF file) to a local file
        with open(localFile,"wb") as fout:
            fout.write(resp.read())

        print("Downloaded file %s." % fileURL)

    except:
        # if the record is unavailable, ignore and try the next day
        print("Encountered exception while trying to download file {0}.".format(fileName))
        pass

    # inject interval between consecutive requests
    time.sleep(5)
