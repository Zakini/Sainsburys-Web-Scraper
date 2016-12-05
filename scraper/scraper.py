from lxml import html
import requests
import json


def scrape(targetUrl):
    htmlTree = getHtml(targetUrl)
    elements = reduceToKeyElements(htmlTree)
    info = [convertToKeyInfo(el) for el in elements]
    infoObj = summarise(info)
    jsonString = json.dumps(infoObj)
    print(jsonString)


def getHtml(targetUrl):
    """Make a GET request to targetUrl
    and return the result as a tree object"""
    pass


def reduceToKeyElements(htmlTree):
    """Strip down htmlTree to a list of the elements we are interested in"""
    pass


def convertToKeyInfo(element):
    """Convert a HTML element into a dictionary of relevant info"""
    pass


def summarise(infoList):
    """Move infoList into a dictionary and with the total of all items"""
    pass
