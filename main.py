from scraper import scrape
from sys import argv, exit


def main():
    if len(argv) < 2:
        print("Error: expected URL")
        exit(1)
    targetUrl = argv[1]

    print(scrape(targetUrl))

    exit(0)


if __name__ == "main":
    main()
