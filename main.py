from bs4 import BeautifulSoup
import re

file = open("Starting strength log.html", encoding="utf8")
soup = BeautifulSoup(file, "html.parser")
# swap to lxml if any emoji related problems occours

# print(soup.prettify())
bodyhtml = soup.find("body")
# print(bodyhtml.prettify())
divtag = bodyhtml.find('div')

#print(divtag.prettify())

# (.*september).\d*  to find month stings
# use this find the individual div tag of the day
#sideway navigation to other div tags contains lifts numbers

#print(divtag.find('September'))

#print(divtag.span.div.next_sibling)

for sibling in divtag.span.div.next_siblings:
    print(sibling)

#sibling[10]

#print(divtag.span.div.find_next_siblings('div'))
