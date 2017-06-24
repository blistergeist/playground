# beautifulsoup_practice.py
import urllib.request
import requests
from bs4 import BeautifulSoup

# html = urllib.request.urlopen('http://money.cnn.com/2016/12/23/technology/consumer-reports-macbook-pro/index.html')
html = requests.get('http://money.cnn.com/2016/12/23/technology/consumer-reports-macbook-pro/index.html')
print(html.text)
soup = BeautifulSoup(html.text, 'lxml')

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# # print(soup.find_all('p'))
# # print(soup.find_all('a'))
# print(soup.find(href='https://www.lendingtree.com'))
# a = soup.find_all('a')
# for tag in a:
# 	print(tag.attrs)

# for link in soup.find_all('a'):
# 	print(link.get('href'))

print(soup('script') == soup.find_all('script'))

print(len(soup.find_all('script')))
print(len(soup.find_all('style')))
for script in soup(['script']):
	script.extract()
print(len(soup.find_all('script')))
# iterTag = soup.html
# for i in range(5):
# 	iterTag = iterTag.next_element
# 	print(iterTag.next_element)


# figure out how to filter out only the valid usable text
# this is generally found in <p> (paragraph) tags 
# why do you take out scripts and styles?
# what are scripts and styles? 
# a script is just that, code that does something client-side
# a style affects how text is displayed for a given tag (color, size, etc.) 
# I may be able to use find_parents() and find_siblings() to find valid text