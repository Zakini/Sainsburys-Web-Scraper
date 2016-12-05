from scraper import scrape
from sys import argv


def main():
    targetUrl = argv[1]
    scrape(targetUrl)


if __name__ == "main":
    main()
