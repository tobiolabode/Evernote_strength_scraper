from bs4 import BeautifulSoup
import re
import itertools

file = open("Starting strength log.html", encoding="utf8")
soup = BeautifulSoup(file, "html.parser")
# swap to lxml if any emoji related problems occours

# print(soup.prettify())
bodyhtml = soup.find("body")
# print(bodyhtml.prettify())
# print(bodyhtml.div.span.div.next_sibling.prettify())

for sibling in bodyhtml.div.span.div.next_siblings:
    print(sibling)
