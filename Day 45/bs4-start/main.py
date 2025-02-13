from bs4 import BeautifulSoup


with open('website.html') as file:
    data = file.read()

soup = BeautifulSoup(data, "html.parser")

# print(soup) # All data without indent

# print(soup.title) # Data with html tag

# print(soup.title.string) # inner data without html tag

#print(soup.prettify())  # prettify() makes all html code indent

# print(soup.a) # it's print the first a tag (p, form, li and .....)