from bs4 import BeautifulSoup
import re
import itertools

file = open("Starting strength log.html", encoding="utf8")
soup = BeautifulSoup(file, "html.parser")
# swap to lxml if any emoji related problems occours

# print(soup.prettify())
bodyhtml = soup.find("body")
# print(bodyhtml.prettify())
divtag = bodyhtml.find('div')

inner_div_tag = divtag.span.div

# print(divtag.prettify())

# (.*september).\d*  to find month stings
# use this find the individual div tag of the day
# sideway navigation to other div tags contains lifts numbers

# print(divtag.find('September'))

# print(divtag.span.div.next_sibling)

sibling_contents = []
for sibling in inner_div_tag.next_siblings:
    # print(sibling)
    sibling_contents.append(sibling.contents)
    print(sibling.contents)
print('\n --------------------------- \n')
print("Results of list")
print(sibling_contents)

sibling_contents = list(itertools.chain(*sibling_contents))
print('\n --------------------------- \n')
print('\n --------------------------- \n')
print('\n --------------------------- \n')
print(sibling_contents)




# sibling[10]

# print(divtag.span.div.find_next_siblings('div'))
