# Copyright 2014, Radhika S. Saksena (radhika dot saksena at gmail dot com)
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Web scraping and text processing with Python workshop

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.exceptions import CloseSpider
import sys
import re
import os

"""Define a spider which searches for all the statements and speeches made 
    by the 96-th Japanese PM in 2013. The relevant HTML documents once found 
    are then saved locally."""

"""Note that this .py file goes in to the spiders/ directory in the Scrapy project setup.
    Refer to workshop notes for more details on where this file should be located."""

class KanteiSpider(CrawlSpider):
    name = "Kantei"
    allowed_domains = ["kantei.go.jp"]
    start_urls = [
            "http://www.kantei.go.jp/foreign/96_abe/statement/index_e.html"
    ]

    rules = (
            Rule(SgmlLinkExtractor(allow=(re.compile("2013.*\/index.*\.html"))),callback='parse_item',follow=True),
            Rule(SgmlLinkExtractor(allow=(re.compile("2013.*\/.*\.html"))),callback='press_item',follow=False),
            Rule(SgmlLinkExtractor(allow=(re.compile("2013"))),callback='parse_item',follow=True),)

    def press_item(self, response):
        print("press_item: Next link is %s" % response.url)

        outputDir = "archives"

        #construct name of output file
        matchObj = re.search("http:\/\/(.*)$",response.url)
        outputfileName = "%s/%s" % (outputDir,re.sub("\/","_",matchObj.group(1)))
        print "Saving file %s." % outputfileName

        if not os.path.exists(outputDir):
            os.makedirs(outputDir)

        fout = open(outputfileName,"w")
        fout.write(response.body)
        fout.close

    def parse_item(self, response):
        print("parse_item: Next link is %s" % response.url)
