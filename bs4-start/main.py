from bs4 import BeautifulSoup
import lxml
with open("/Users/apple/umeraziz/pandas-python-csv/bs4-start/website.html", "r") as file:
    content = file.read()
    # print(content)

# soup = BeautifulSoup(content , lxml)
soup = BeautifulSoup(content , "html.parser")
# print(soup.title.string)
# print(soup.prettify)
# print(soup.a)

all_a = soup.find_all(name="h1 em")
# print(all_a.get("Text"))

# for tag in all_a:
#     # print(tag.getText())
#     print(tag.get("href"))



print(soup.find_all("a"))