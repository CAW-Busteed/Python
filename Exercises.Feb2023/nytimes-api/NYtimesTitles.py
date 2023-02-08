'''
use beautiful soup and requests to print out a list of the NY times titles
fetch the site as HTML
parse HTML for titles
figure out what marks the titles, and isolate them
print titles on request


'''
import requests
from bs4 import BeautifulSoup

#fetching from site
r = requests.get('https://www.nytimes.com/')

#this should parse r into  HTML
SOUP = BeautifulSoup(r, 'html.parser')


print(SOUP.prettify())
