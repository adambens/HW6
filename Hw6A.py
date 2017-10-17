from urllib.request import urlopen 
from bs4 import BeautifulSoup 
import re 
import ssl

url = input("Enter a url: ")
html = urlopen(url).read() 
num_count = []

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

soup = BeautifulSoup(html, 'html.parser')

for tag in soup.find_all('span'):
	tag = str(tag)
	tags = tag.split('>')[1]
	last_split= tags.split('<')
	num_count.append(int(last_split[0]))

print("Count:", len(num_count))
print("Sum:", sum(num_count))


"""
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html_doc = urlopen(url, context=ctx).read()

count = []
soup = BeautifulSoup(html_doc, 'html.parser')
for tag in soup.find_all('span'):
	tag = str(tag)
	x = tag.split('>')[1]
	y = x.split('<')
	count.append(int(y[0]))
print('Sum: ', sum(count))
"""