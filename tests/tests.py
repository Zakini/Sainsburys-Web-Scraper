import unittest
import scraper
from lxml import html
import requests
import json


# not really a unit test, but testing this should be simple
class test_scraper_scrape(unittest.TestCase):
    def test_requestOk(self):
        targetUrl = ("http://hiring-tests.s3-website-eu-west-1.amazonaws.com/"
                     "2015_Developer_Scrape/5_products.html")

        result = json.loads(scraper.scrape(targetUrl))

        jsonFile = open("tests/expected.json")
        expectedResult = json.loads(jsonFile.read())
        jsonFile.close()

        self.assertEqual(result, expectedResult)

    def test_requestInvalidUrl(self):
        with self.assertRaises(requests.exceptions.MissingSchema):
            scraper.scrape("aivadriljvbla")
        with self.assertRaises(requests.ConnectionError):
            scraper.scrape("http://aijvbjirbvl")

    def test_requestWrongSite(self):
        result = json.loads(scraper.scrape("http://www.google.co.uk"))
        expectedResult = {"results": [], "total": 0}
        self.assertEqual(result, expectedResult)


class test_scraper_convertToKeyInfo(unittest.TestCase):
    def test_correctElement(self):
        htmlFile = open("tests/test.html")
        self.targetElement = html.fromstring(htmlFile.read())
        htmlFile.close()

        result = scraper.convertToKeyInfo(self.targetElement)

        expectedResult = {
            "title": "Sainsbury's Conference Pears, Ripe & Ready x4 (minimum)",
            "unit_price": 1.5,
            "size": "39.465kB",
            "description": "Conference"
        }

        self.assertEqual(result, expectedResult)

    def test_incorrectElement(self):
        element = html.fromstring("<p>not the tag you are looking for</p>")
        with self.assertRaises(ValueError):
            scraper.convertToKeyInfo(element)


class test_scraper_summarise(unittest.TestCase):
    def test_correctList(self):
        targetList = [
            {
                "unit_price": 42.3
            },
            {
                "unit_price": 0.34
            },
            {
                "unit_price": 1.76
            }
        ]

        expectedResult = {
            "total": 44.4,
            "results": targetList
        }

        self.assertEqual(scraper.summarise(targetList),
                         expectedResult)

    def test_incorrectList(self):
        targetList = [{}, {}, {}]

        with self.assertRaises(KeyError):
            scraper.summarise(targetList)
