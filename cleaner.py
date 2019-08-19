import pandas as pd
import numpy as np
import re

# pd.set_option('display.max_columns', 10)

regex_deadlift = re.compile(r'.*(d?ead).*')
regex_bench = re.compile(r'.*(B?ench).*')
regex_press = re.compile(r'.*(Pr)[^April].*|.*(pr)[^April].*')

df = pd.read_csv('lifts.csv')
print(df.head())

filter_mask = df['Press'] == df.Press.str.match(regex_deadlift), df.Deadlift
filter_mask2 = df['Deadlift'] == df.Deadlift.str.match(regex_bench), df.Bench

print(df.loc[66:88, ['Date', 'Press']])
print(df.loc[66:88, ['Date', 'Deadlift']])

df['Deadlift'] = np.where(df['Deadlift'] == df.Deadlift.str.contains(regex_bench), df.Bench, df['Deadlift'])
df['Press'] = np.where(df['Press'] == df.Press.str.contains(regex_deadlift), df.Deadlift, df['Press'])

# check if in column correct value
# if not check for value in the rest of the column
# ex. bench 15 found in press, find press value from rest of the columns in the row
# Swap values
# move on
# global val
# val = 'TEST'


def organiser(row):
    try:
        if not regex_press.search(row['Press']):
            if regex_press.search(row['Deadlift']):
                    return row['Deadlift']
            elif regex_press.search(row['Bench']):
                    return row['Bench']
            elif regex_press.search(row['Power clean']):
                    return row['Power clean']

        elif not regex_deadlift.search(row['Deadlift']):
            if regex_deadlift.search(row['Bench']):
                    return row['Bench']
            elif regex_deadlift.search(row['Power clean']):
                    return row['Power clean']
            elif regex_deadlift.search(row['Press']):
                    return row['Press']
        else:
            return 'TEST'
    except TypeError:
        pass

#
# def f(row):
#     try:
#         if row['Bench'] == row['Press']:
#             val = 0
#         elif regex_deadlift.search(row['Press']):
#             val = 1
#         else:
#             val = -1
#     except TypeError:
#         pass
#     return val


# import pdb; pdb.set_trace()
# df['Press'] = df.apply(organiser, axis=1)
# df['Deadlift'] = df.apply(organiser, axis=1)



# print(df.where(filter_mask, inplace=True))


print(df.loc[66:88, ['Date', 'Press']])
print(df.loc[66:88, ['Date', 'Deadlift']])



print('\n ------------------------------ \n ' * 10)

regexfilter = ['[a-zA-Z]', '✔️', '❌', '➡️', '😕', ':', '\(.*\)', '✖️', '/']
# df['Date'] = df['Date'].map(lambda x: x.strip(':'))
df['Squat'] = df['Squat'].str.replace(r'|'.join(regexfilter), '')
df['Press'] = df['Press'].str.replace(r'|'.join(regexfilter), '')
df['Deadlift'] = df['Deadlift'].str.replace(r'|'.join(regexfilter), '')
df['Bench'] = df['Bench'].str.replace(r'|'.join(regexfilter), '')
df['Power clean'] = df['Power clean'].str.replace(r'|'.join(regexfilter), '')


df['Squat'] = df['Squat'].str.replace(r"\(.*\)", "")
df['Press'] = df['Press'].str.replace(r"\(.*\)", "")
df['Deadlift'] = df['Deadlift'].str.replace(r"\(.*\)", "")
df['Bench'] = df['Bench'].str.replace(r"\(.*\)", "")
df['Power clean'] = df['Power clean'].str.replace(r"\(.*\)", "")


df['Squat'] = df['Squat'].str.strip()
df['Press'] = df['Press'].str.strip()
df['Deadlift'] = df['Deadlift'].str.strip()
df['Bench'] = df['Bench'].str.strip()
df['Power clean'] = df['Power clean'].str.strip()

print('\n ------------------------------ \n ' * 10)

# print(df.head())
df.to_csv('lifts_clean.csv', index=False, encoding='utf-8')
