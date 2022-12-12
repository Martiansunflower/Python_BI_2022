#!/usr/bin/env python
# coding: utf-8

import re
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Parse the file using regular expressions and write all ftp links from there into the ftps file

with open('references') as references:
    total = references.read()
    regexp1 = re.compile('ftp\.[./#\w]*')
    ftp = regexp1.findall(total)
    with open('../HW6_RegExpression/ftps', 'w') as ftps:
        print(ftp, file=ftps, sep = '\n')

# 2. Extract all the numbers from the story 2430 A.D.

with open('2430AD') as story:
    total = story.read()
    regexp2 = re.compile('\d{1,}\S\d{1,}|\d{1,}')
    print(regexp2.findall(total))
    print(set(regexp2.findall(total)))

# 3. Extract all the words that have the letter 'a' or 'A' in them 

regexp3 = re.compile('[aA]\w*')
print(regexp3.findall(total))

# 4. Extract all exclamatory sentences.

regexp4 = re.compile('[A-Z][\w\s]*!')
print(regexp4.findall(total))

# 5. Build a distribution histogram of the lengths of unique words.

regexp5 = re.compile('[a-zA-Z]\w*')
words = regexp5.findall(total)
#2942 words at all
lower_words = [x.lower() for x in words]
uniq_words = list(set(lower_words))
#919 unique words
len_words = [len(x) for x in uniq_words]

#I used seaborn first 
sns_plot = sns.histplot(len_words, discrete=True)
fig = sns_plot.get_figure()

#but I couldn't find a way to add labels to axes without changing the data
#So I also used Matplotlib for sure

plt.figure(figsize=(8,6))
plt.hist(len_words, bins = 15)
plt.xticks(range(1,16))
plt.title('Distribution of words\' length' , size = 14)
plt.xlabel('Length')
plt.ylabel('Frequency')

# 6. Make a translator function from Russian to "brick language"

def Translator(rus_str):
    sonorn = 'АаЕеЁёИиОоУуЭэЫыЮюЯя'
    for i in sonorn:
        rus_str = re.sub(f'{i}', f'{i}К{i.upper()}', rus_str)
    return rus_str

Translator('~Нам пора отпустить синиц, нам пора ловить журавлей')

