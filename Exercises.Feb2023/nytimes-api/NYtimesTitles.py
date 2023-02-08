'''
use beautiful soup and requests to print out a list of the NY times titles
fetch the site as HTML
parse HTML for titles
figure out what marks the titles, and isolate them
print titles on request


'''
import requests
from bs4 import BeautifulSoup

#base url to grab
base_url = 'http://www.nytimes.com/'

#fetching from site
r = requests.get(base_url)

# #this should parse r into  HTML
SOUP = BeautifulSoup(r.text, features="html.parser")

for x in SOUP.find_all(class_=["indicate-hover"]):
    print(f"- {x.text}")


