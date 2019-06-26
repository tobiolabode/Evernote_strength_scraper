from bs4 import BeautifulSoup
import re

file = open("Starting strength log.html", encoding="utf8")
soup = BeautifulSoup(file, "html.parser")
# swap to lxml if any emoji related problems occours

# print(soup.prettify())
bodyhtml = soup.find("body")
# print(bodyhtml.prettify())
divtag = bodyhtml.find('div')

print(divtag.prettify())

# (.*september).\d*  to find month stings
# use this find the individual div tag of the day
