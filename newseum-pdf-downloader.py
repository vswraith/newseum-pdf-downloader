#!/usr/bin/env python
"""
    Newseum PDF Downloader
    2014 Mark Norgren

    Edit PAPERS list to add the paper for download
    PAPERS are downloaded to a 'downloads' directory in current working directory
    Get paper names at: http://www.newseum.org/todaysfrontpages/
    Follow the 'Readable PDF' link
"""
import urllib2
import cookielib
import os
import time
import asyncore

# Papers list for download
PAPERS = ["MN_ST", "MN_PP", "ND_TF", "ND_GFH", "NY_NYT"]

NEWSEUM_PDF_URL="http://webmedia.newseum.org/newseum-multimedia/dfp/pdf22/{0}.pdf"
NEWSEUM_IMG="http://www.newseum.org"

def fetchTodaysPDFFor(paper):
    """
    Fetch the PDF for a paper
    """
    print "Grabbing frontpage for %s" % (paper)
    todaysDate = time.strftime("%Y.%m.%d")

    directory = "downloads"
    if not os.path.exists(directory):
        os.makedirs(directory)

    fileName = os.path.join("downloads", "%s-%s.pdf" % (paper, todaysDate))

    page = NEWSEUM_PDF_URL.format(paper)
    print "page URL: %s" % (page)
    f = urllib2.urlopen(page)
    with open(fileName, 'wb') as file:
        file.write(f.read())
    f.close()
    

def main():
    for paper in PAPERS:
        fetchTodaysPDFFor(paper)


if __name__ == '__main__':
    main()


