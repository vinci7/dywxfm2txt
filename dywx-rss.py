import os
from urllib.request import urlopen
from xml.etree.ElementTree import parse


# Download the RSS feed and parse it
dirName = "dywx-audio"
project = "dywx"
rss = "http://rss.lizhi.fm/rss/1959617.xml"


downloadFlag = -1

def initDownloadFlag():
    c = input("Audio didn't existed, download?[y/N]")
    downloadFlag = 1 if isY(c) else 0

def isY(chr):
    if ((chr=='y') or (chr=='Y')):
        return True
    return False

def checkDir(dirName):
    if not os.path.exists(dirName):
        c = input("Directory {} didn't existed, create?[y/N]".format(dirName))
        if isY(c):
            os.makedirs(dirName)

def getFileType(path):
    return path.split('.')[-1]

def download(url, fileName):
    f = urlopen(url)
    if not os.path.exists(fileName):
        with open(fileName, "wb") as code:
            code.write(f.read())

def getIndex(title):
    l = title.find('#')
    r = title.find('：')
    index = title[l+1:r] 
    if not index.isdigit():
        index = 0
    return index




u = urlopen(rss)
doc = parse(u)
checkDir(dirName)


# Extract and output tags of interest
for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    date = item.findtext('pubDate')
    description = item.findtext('description')
    guid = item.findtext('guid')

    print(title)

    index = getIndex(title)
    print(index)
    
    print(date)
    print(description)
    print(guid)

    fileType = getFileType(guid)
    fileName = "{}/{}{}.{}".format(dirName, project, index, fileType)

    if not os.path.exists(fileName):
        if downloadFlag == -1:
            initDownloadFlag()
        if downloadFlag:
            download(guid, fileName)

    print()


