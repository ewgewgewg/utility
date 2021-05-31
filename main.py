from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
from sources import sources
from actions import actions


exclude = ['{','()','©']

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    if len(element.split()) < 5:
        return False
    if any(sub in element for sub in exclude):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return "\n".join(t.strip() for t in visible_texts)

#html = urllib.request.urlopen('https://www.nytimes.com').read()
#print(text_from_html(html))

for source in sources:
  print(source["link"])
  html = urllib.request.urlopen(source["link"]).read()
  print(text_from_html(html))

#works!

def data():
  results = []
  for source in sources:
    results.append(source["link"])
    html = urllib.request.urlopen(source["link"]).read()
    results.append(text_from_html(html))
  return " ".join(result for result in results)


actions(data)















# #This will not run on online IDE
# import requests
# import re
# from bs4 import BeautifulSoup
  
# URL = "http://www.nytimes.com"
# r = requests.get(URL)
  
# soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
# # print(soup.prettify())

# # for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
# #     print(link.get('href'))
