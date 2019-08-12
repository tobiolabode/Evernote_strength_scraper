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
regex_press = re.compile(r'.*(Pr)[^April].*|.*(pr)[^April].*')
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
master_regex = re.compile(r'.*(?:Pr)[^April].*|.*(?:pr)[^April].*|(?:Sq).*|(?:sq).*|.*(?:d?ead).*|.*(?:B?ench).*|.*(?:P?ower).*')

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


# turning values to csv loop
# if value(list) has an nested list inside
# run isinstance to extract the data
print("\n ------------------------------- \n ")
print("\n ------------------------------- \n ")
print("\n ------------------------------- \n ")


value_to_list = []
for lists in threelist2:
    for value in lists:

        if isinstance(value, list):
            # print(f"{value[0]}, nested-list")

            if master_regex.search(value[0]):
                print(f'{value[0]}, lift')
                value_to_list.append(value[0])
            else:
                print(f'{value[0]}, non-lift')
                value_to_list.append(value[0])

            continue

        if regex_dates.search(value):
            print("\n")
            print(f"{value}, Date")
            value_to_list.append(value)
        if regex_squat.search(value):
            print(f"{value}, lift")
            value_to_list.append(value)

        elif regex_press.search(value):
            print(f"{value}, lift")
            value_to_list.append(value)

        elif regex_deadlift.search(value):
            print(f"{value}, lift")
            value_to_list.append(value)

        elif regex_bench.search(value):
            print(f"{value}, lift")
            value_to_list.append(value)

        elif regex_power_clean.search(value):
            print(f"{value}, lift")
            value_to_list.append(value)

print("\n ------------------------------- \n ")
print("\n ------------------------------- \n ")
print("\n ------------------------------- \n ")
print("\n ------------------------------- \n ")
print("\n ------------------------------- \n ")
print("\n ------------------------------- \n ")


print(value_to_list)
for i in value_to_list:
    print(i)

# i = 0
# value_to_list2 = []
# while i < len(value_to_list):
#     value_to_list2.append(value_to_list[i:i+4])
#     i += 4
#
#
# print(f"new list:{value_to_list2}")
# print("\n ------------------------------- \n " * 5)
#
# for i in value_to_list2:
#     print(i)

print("\n ------------------------------- \n " * 5)

header = ["Date", "Squat", "Press", "Deadlift", "Bench", "Power clean", "notes"]
with open('lifts.csv', mode='w', encoding='utf-8') as lifts_file:
    lifts_writer = csv.writer(lifts_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    lifts_writer.writerow(header)
    values_to_row = []

    # for item in range(7):
    #     values_to_row.append('TEST')

    for values in value_to_list:
        if regex_dates.search(values):
                values_to_row.append(values)

        elif regex_squat.search(values):
                values_to_row.append(values)

        elif regex_press.search(values):
                values_to_row.insert(2, values)
                # try:
                #     for value in values_to_row:
                #         if value != regex_press.search(values):
                #             values_to_row.insert(2, 'TEST')
                # except IndexError as error:
                #     print(error)
                #     continue

        elif regex_deadlift.search(values):
                values_to_row.insert(3, values)

        elif regex_bench.search(values):
                values_to_row.insert(4, values)

        elif regex_power_clean.search(values):
                values_to_row.append(values)

        # if re.search('October 4', values):
        #     lifts_writer.writerow(values_to_row)
        #     if re.search('Deadlift: ---', values):
        #         break

        if re.search('---', values) or re.search('pra', values) or re.search('forgot', values):
            lifts_writer.writerow(values_to_row)
            print(values_to_row)
            values_to_row.clear()

        if re.search('Tick', values):
            for column in range(6):
                values_to_row.insert(0, None)
            lifts_writer.writerow(values_to_row)
            print(values_to_row)
            values_to_row.clear()



        if len(values_to_row) > 3 and regex_dates.search(values_to_row[0]):

            # exceptions order
            if values_to_row[0] == 'September 27:':
                values_to_row.insert(4, 'TEST')
                values_to_row.insert(5, 'TEST')
            if values_to_row[0] == '21 April':
                values_to_row.insert(3, values_to_row[2])
                values_to_row.pop(2)
                values_to_row.insert(2, 'TEST')
            #     values_to_row.insert(4, values_to_row[3])
            #     values_to_row.pop(3)
            #     values_to_row.insert(3, 'TEST')

            # Bench
            if regex_bench.search(values_to_row[2]):
                values_to_row.insert(4, values_to_row[2])
                values_to_row.pop(2)
                values_to_row.insert(2, 'TEST')
                values_to_row.insert(6, 'TEST')

            if regex_power_clean.search(values_to_row[3]):
                values_to_row.insert(5, values_to_row[3])
                values_to_row.pop(3)
                values_to_row.insert(3, 'TEST')
                values_to_row.insert(4, 'TEST')



            # if regex_deadlift.search(values_to_row[3]):
            #     values_to_row.insert(5, 'TEST')

            # if value pasts theresolod of chars, silpt after nth amount of charcters.
            # squat 10 chars

            if regex_squat.search(values_to_row[1]):
                if len(values_to_row[1].replace('✔️', '')) > 14:
                    values_to_row.insert(7, values_to_row[1])
                else:
                    pass
            if regex_press.search(values_to_row[2]) and not (regex_ticks.search(values_to_row[2])):
                if len(values_to_row[2]) > 9:
                    values_to_row.insert(7, values_to_row[2])
                else:
                    pass
            if regex_deadlift.search(values_to_row[3]) and not (regex_ticks.search(values_to_row[3])):
                if len(values_to_row[3]) > 13:
                    values_to_row.insert(7, values_to_row[3])
                else:
                    pass
            try:
                if regex_bench.search(values_to_row[4]) and not (regex_ticks.search(values_to_row[4])):
                    if len(values_to_row[4]) > 10:
                        values_to_row.insert(7, values_to_row[4])
                    else:
                        pass
            except IndexError:
                pass

            try:
                if regex_power_clean.search(values_to_row[5]) and not (regex_ticks.search(values_to_row[5])):
                    if len(values_to_row[5]) > 15:
                        values_to_row.insert(7, values_to_row[5])
                    else:
                        pass
            except IndexError:
                pass

                # making adtempts column to places the ticks ex: squat adtempts, benc adtempts

            lifts_writer.writerow(values_to_row)
            print(values_to_row)
            values_to_row.clear()
        else:
            pass




# idea turn emojis into digits of number of adtempts
# print len of 4 unless last value is date
