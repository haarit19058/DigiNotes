# Setting up the environment
- pip install requests
	- to manage requests to any url
- pip install html5lib
	- parse the data
- pip install bs4

# Fetching the html content
- Fetch the content

# Parse the HTML

# HTML tree traversal


# Let's code

If you want to scrape a website
1) Use the API
2) HTML web scraping using some tool

```python
import requests
from bs4 import BeautifulSoup
url="https://codewithharry.com"


#step1: Get the HTML
r = requests.get(url)
htmlcontent = r.content

#step2: parse the html
soup = BeautifilSoup(htmlccontent,"html.parser")
print(soup)

#step3: HTML Tree traversal
title=soup.title
print(title,type(title)) # gives the tag as type

print(title.string,type(title.string)) # navigable string

# Commonly used types of objects:
# 1. Tag
print(title)
# 2. NavigableString
print(title,string)
# 3. BeautifulSoup
print(type(soup))
# 4. Comment


#get all paragraphs from the webpage
paras = soup.find_all('p')
print(paras)

#get all anchor tags from the webpage
anchor=soup.find_all('a')
print(anchor)

print(soup.find('p')) # gives the first para
print(soup.find('p')['class'])  # gives the classes of the object

# find all the elements whose class is lead
print(soup.find_all('p',class_="lead"))


# get the text from the elements
print(soup.find('p').get_text())

#get all the links on the page
anchors=soup.find_all('a')
all_links=set()
for link in anchors:
	if (link != "#") :
		linkText='https://codewithharry.com'+ link.get('href')
		all_links.add(linkText)
		print(linkText)


markup = "<p><!--this is a comment --></p>"

soup2 = BeautifulSoup(markup)
print(soup2.p.string)
print(type(soup2.p.string))


nsc=soup.find(id="navbarSupportedContent")
print(nsc.children)

print(nsc.contents) # gives all the content inside the tag

# .contents - A tag's children are available as a list
# .children - A tag's children are availabel as a generator




```

# Content

```python
```