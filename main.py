from bs4 import BeautifulSoup
import re
import itertools
import csv



file = open("Starting strength log.html", encoding="utf8")
soup = BeautifulSoup(file, "html.parser")
# swap to lxml if any emoji related problems occours

# print(soup.prettify())
bodyhtml = soup.find("body")
# print(bodyhtml.prettify())
divtag = bodyhtml.find('div')

inner_div_tag = divtag.span.div

# print(divtag.prettify())

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


regex = re.compile(r'<.br>|<br.>')
sibling_contents_string_without_br = [item for item in sibling_contents_string
                                      if not regex.match(item)]

# print(sibling_contents_string_without_br[8:])
sibling_contents_clean = sibling_contents_string_without_br[8:]
# print(sibling_contents_clean)

regex_dates = re.compile(r'(Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)', flags=re.IGNORECASE)
regex_squat = re.compile(r'(Sq).*|(sq).*')
regex_press = re.compile(r'.*(Pr).*|.*(pr).*')
regex_deadlift = re.compile(r'.*(d?ead).*')
regex_bench = re.compile(r'.*(B?ench).*')
regex_power_clean = re.compile(r'.*(P?ower).*')
regex_other_html = re.compile(r'<[^>]*>')
regex_ticks = re.compile(r'.*(✔️)')
regex_crosses = re.compile(r'.*(❌)')

Dateslist = [date for date in sibling_contents_clean if regex_dates.match(date)]
# print(Dateslist)
list_squat = [squat for squat in sibling_contents_clean if regex_squat.match(squat)]
# print(list_squat)
Notes_squat_list = []
for squat in list_squat:
    if len(squat) > 25:
        if regex_crosses.match(squat):
            Notes_squat_list.append(squat)
        if not regex_ticks.match(squat):
            Notes_squat_list.append(squat)

# print(Notes_squat_list)
Press_list = [press for press in sibling_contents_clean if regex_press.match(press)]
# print(Press_list)


Notes_press_list = []
for Press in Press_list:
    if len(Press) > 25:
        if regex_crosses.match(Press):
            Notes_press_list.append(Press)
        if not regex_ticks.match(Press):
            Notes_press_list.append(Press)

# print(Notes_press_list)

deadlift_list = [deadlift for deadlift in sibling_contents_clean if
                 regex_deadlift.match(deadlift)]
# print(deadlift_list)


Notes_deadlift_list = []
for deadlift in deadlift_list:
    if len(deadlift) > 25:
        if regex_crosses.match(deadlift):
            Notes_deadlift_list.append(deadlift)
        if not regex_ticks.match(deadlift):
            Notes_deadlift_list.append(deadlift)

# print(Notes_deadlift_list)


Bench_list = [bench for bench in sibling_contents_clean if regex_bench.match(bench)]
# print(Bench_list)


Notes_bench_list = []
for bench in Bench_list:
    if len(bench) > 25:
        if regex_crosses.match(bench):
            Notes_bench_list.append(bench)
        if not regex_ticks.match(bench):
            Notes_bench_list.append(bench)

# print(Notes_bench_list)

Power_clean_list = [power_clean for power_clean in sibling_contents_clean
                    if regex_power_clean.match(power_clean)]
# print(Power_clean_list)

# Notes_power_clean_list = [power_clean for power_clean in Power_clean_list if len(power_clean) > 25 if not regex_ticks.match(power_clean)]
# import pdb; pdb.set_trace()

Notes_power_clean_list = []
for power_clean in Power_clean_list:
    if len(power_clean) > 25:
        if regex_crosses.match(power_clean):
            Notes_power_clean_list.append(power_clean)
        else:
            pass
        if not regex_ticks.match(power_clean):
            Notes_power_clean_list.append(power_clean)


# print(Notes_power_clean_list)

zipped = zip(Dateslist, list_squat)
zipped = set(zipped)
# print(zipped)


threelist = [sibling_contents_clean[i:i+4] for i in range(0,
             len(sibling_contents_clean), 4)]


listcounter = 0
i = 0
threelist2 = []
'''
if first value of the list is not a date then use sibling_contents_clean[i+1:i+5]
then + 1 to i
append value to prevois list
after + 4 to i

'''
regexlist = [regex_squat, regex_press, regex_deadlift, regex_bench, regex_power_clean]
master_regex = re.compile(r'.*(?:Pr).*|.*(?:pr).*|(?:Sq).*|(?:sq).*|.*(?:d?ead).*|.*(?:B?ench).*|.*(?:P?ower).*')

while i < len(sibling_contents_clean):
    if regex_dates.search(sibling_contents_clean[i]):
        threelist2.append(sibling_contents_clean[i:i+4])
        print(f"correct, {sibling_contents_clean[i]}")

    elif master_regex.search(sibling_contents_clean[i]):
            print(f"incorrect, {sibling_contents_clean[i]}")
            lenoflist = len(threelist2)
            print(f' length of list: {lenoflist}')
            threelist2[lenoflist-1].append(sibling_contents_clean[i:i+1])
            threelist2.append(sibling_contents_clean[i+1:i+5])
            i += 1

    else:
        print(f"incorrect, non-lift, {sibling_contents_clean[i]}")
        threelist2.append(sibling_contents_clean[i:i+1])
        i += 1

    i += 4

# threelist2 = list(itertools.chain(*threelist2))


print("\n ------------------------------- \n ")
contentnumber = 0
for item in threelist2:
    print(f"{item}, {contentnumber}")
    contentnumber += 1




# with open('lifts.csv', mode='w') as lifts_file:
#     lifts_writer = csv.writer(lifts_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)






# idea turn emojis into digits of number of adtempts
