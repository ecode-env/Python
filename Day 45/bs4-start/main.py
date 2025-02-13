from operator import index

from bs4 import BeautifulSoup
import requests


response = requests.get('https://appbrewery.github.io/news.ycombinator.com/')
response.raise_for_status()

content = response.text

soup = BeautifulSoup(content, 'html.parser')

articles_text = []
articles_link = []



articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)
article_upVotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_upVotes)
print(article_links)
print(article_texts)

inx = article_upVotes.index(max(article_upVotes))


title = article_texts[inx]
link = article_links[inx]

print(inx)
print(title)
print(link)




























# with open('website.html') as file:
#     data = file.read()
#
# soup = BeautifulSoup(data, "html.parser")

# print(soup) # All data without indent

# print(soup.title) # Data with html tag

# print(soup.title.string) # inner data without html tag

#print(soup.prettify())  # prettify() makes all html code indent

# print(soup.a) # it's print the first a tag (p, form, li and .....)

# --------------------------------------------------------------------


# to_find_all = soup.find_all(name='a')
#
# for tag in to_find_all:
#     #print(tag) # to get list of tag
#     #print(tag.getText()) # to get inner tag of text
#     #print(tag.get('href'))  # to get attribute of tag


#------------ To find with ID or class ------------


# heading = soup.find(name='h1', id='name')
# heading = soup.find(name='h3', class_='heading')
#
# print(heading)

# ------------ To select inner tags ----------
# We can use CSS selecting methode in this.

# name = soup.select_one(selector='p em') # inner data
#name = soup.select_one(selector='#name') # with ID name
# name_class = soup.select_one(selector='.heading') # with class name but only the first
#
#
# print(name)

# ---------- To get all data with same name ------


# all_class = soup.select('.heading') # return in array all this tag name called
#
# print(all_class)


