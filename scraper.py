from lxml import html
import requests
import json


def scrape(targetUrl):
    """Module main function

    Makes a GET request to targetUrl and scrapes product info from it
    Returns a JSON string in the following format (not pretty printed):

    {
        "total": 41.99,
        "results": [
            {
                "title": "product title",
                "unit_price": 41.99,
                "size": "42.001kB",
                "description": "product description"
            }
        ]
    }"""
    response = requests.get(targetUrl)
    htmlTree = html.fromstring(response.content)
    keyElements = htmlTree.cssselect(".productInner")
    infoObj = [convertToKeyInfo(el) for el in keyElements]
    infoObj = summarise(infoObj)
    jsonString = json.dumps(infoObj)
    return jsonString


def convertToKeyInfo(element):
    """Convert a HTML element into a dictionary of relevant info"""
    if element.get("class") != "productInner":
        raise ValueError("Invalid argument: element does not appear to contain"
                         " product information")

    infoObj = {}
    linkElement = element.cssselect("a")[0]

    # get title
    infoObj["title"] = linkElement.text.strip()

    # get unit_price
    unitPriceString = element.cssselect(".pricePerUnit")[0].text
    # strip whitespace and remove &pound from start of string
    unitPriceString = unitPriceString.strip()[6:]
    infoObj["unit_price"] = float(unitPriceString)

    # request product page
    productPageUrl = linkElement.get("href")
    response = requests.get(productPageUrl)

    # get size
    productPageKilobytes = len(response.content) / 1000
    infoObj["size"] = str(productPageKilobytes) + "kB"

    # get description
    productPageTree = html.fromstring(response.content)
    # only get the first p element
    descriptionElement = productPageTree.cssselect(".productText p")[0]
    infoObj["description"] = descriptionElement.text.strip()

    return infoObj


def summarise(infoList):
    """Move infoList into a dictionary and with the total of all items"""
    parentDict = {}

    parentDict["results"] = infoList

    # calculate total
    total = sum([obj["unit_price"] for obj in infoList])
    parentDict["total"] = round(total, 2)

    return parentDict
