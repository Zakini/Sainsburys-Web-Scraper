# Sainsburys-Web-Scraper
Python console application to scrape content from Sainsbury's online store and convert it into JSON format.

## Requirements
Required libraries (as listed in `requirements.txt`) are:
* lxml v3.6.4
* requests v2.12.3
* cssselect v1.0.0

## Usage
Run `main.py` followed by the URL to scrape
> python main.py http://www.exa&#58;mple.com
The resulting JSON string will be printed to stdout

To run unit tests, run the standard python `unittest` command in the `tests` directory
> python -m unittest discover -s tests