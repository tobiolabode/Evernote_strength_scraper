from bs4 import BeautifulSoup

soup = BeautifulSoup(open("Starting strength log.html"), "html.parser")

print(soup)
