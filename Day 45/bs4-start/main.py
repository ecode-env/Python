from bs4 import BeautifulSoup


with open('website.html') as file:
    data = file.read()

soup = BeautifulSoup(data, "html.parser")

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

