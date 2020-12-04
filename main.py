#https://www.youtube.com/watch?v=ng2o98k983k&ab_channel=CoreySchafer

from bs4 import BeautifulSoup
import requests
import lxml

source = requests.get('https://coreyms.com/').text

soup = BeautifulSoup(source, 'lxml')

# article = soup.find('article')
# This parses out the first article in the html script using the 'find' function

# print(article.prettify())
# This prints out the article in question

# headline = article.h2.a.text
## The headline 'Python Tutorial: Zip Files - Creating and Extracting Zip Archives' is found under an h2 tag -> a tag -> and we want to pull out the text
# print(headline)

# summary = article.find('div', class_='entry-content').p.text
## This pulls out the summary text, which we use the find function to locate (along with class_ denominator to find the specific content in question)
# print(summary)

# vid_src = article.find('iframe', class_='youtube-player')['src']
# this allows us to look for the video source i.e. youtube URL...the ['src'] acts as a dictionary to pull the source from 'article'
# print(vid_src)



