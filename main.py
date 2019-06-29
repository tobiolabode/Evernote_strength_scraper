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

inner_div_tag_text = inner_div_tag.get_text()


sibling_contents = []
for sibling in inner_div_tag.next_siblings:
    # text_content = sibling.find('').text
    # print(text_content)

    # print(sibling)
    sibling_contents.append(sibling.contents)
    # print(sibling.contents)

print('\n --------------------------- \n')
print("Results of list")
# print(sibling_contents, sep='\n')

sibling_contents = list(itertools.chain(*sibling_contents))
print('\n --------------------------- \n')
print('\n --------------------------- \n')
print('\n --------------------------- \n')
# print(sibling_contents)

# print(sibling_contents[20])
# print(type(sibling_contents[20]))
# print(sibling_contents[19])
# print(type(sibling_contents[19]))


sibling_contents_string = []
for item in sibling_contents:
    item = str(item)
    sibling_contents_string.append(item)


# print(sibling_contents_string)
# print(sibling_contents_string[19])
# print(type(sibling_contents_string[19]))
# print(sibling_contents_string[20])
# print(type(sibling_contents_string[20]))


# sibling_contents_string_without_br = []
# for item in sibling_contents_string:
#     if item == '</br>' or '<br/>':
#         sibling_contents_string.remove(item)

regex = re.compile(r'<.br>|<br.>')
sibling_contents_string_without_br = [item for item in sibling_contents_string
                                      if not regex.match(item)]

# print(sibling_contents_string_without_br[8:])
sibling_contents_clean = sibling_contents_string_without_br[8:]
print(sibling_contents_clean)






# for item in sibling_contents:
#     if item == isinstance(bs4.element.Tag):
#         item = str(item)
#
# print(sibling_contents)




# # def cleanhtml(raw_html):
# #     cleanr = re.compile('<.*?>')
# #     cleantext = re.sub(cleanr, '', raw_html)
# #     return cleantext
#
#
# sibling_contentsV2 = sibling_contents
# for item in sibling_contents:
#     if item == pass:
#         sibling_contents.remove(item)
#         sibling_contentsV2 = sibling_contents
#
#
# print('\n --------------------------- \n')
# print('\n --------------------------- \n')
# print('\n --------------------------- \n')
# print(sibling_contentsV2)






# sibling[10]

# print(divtag.span.div.find_next_siblings('div'))
