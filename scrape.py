from unittest.util import sorted_list_difference
from urllib.request import urlopen
from bs4 import BeautifulSoup


def extract_number(s):
    return int(s.split()[-1])

#i will be using the BeautifulSoup library to parse the HTML and extract the data from the webpage.
url = ("https://pl.wikipedia.org/wiki/Muzea_w_Polsce")
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
max_word_count = 0
site_list = []
iteration = 0
for tag in soup.find_all('a', href=True):
    if tag['href'].startswith('/wiki/'):
        url = ("https://pl.wikipedia.org" + tag['href'])
        muzeum_site = urlopen(url)
        muzeum_soup = BeautifulSoup(muzeum_site, 'html.parser')
        words = muzeum_soup.get_text().split()
        word_count = len(words)
        iteration += 1
        print(iteration)
        site_list.append(tag.get_text() + " " + str(word_count))
sorted_list = sorted(site_list, key=lambda x: extract_number(x))
inverted_list = sorted_list[::-1]
print(inverted_list)



