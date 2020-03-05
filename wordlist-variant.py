#!/usr/bin/env python
"""

DESCRIPTION

    Python script which will import a text list of words and add variants of each word to the list

EXAMPLES

    wordlist-variant.py

AUTHOR

    Jeff Stein <jeff@sioblog.net>
    March, 2020

LICENSE

    licensed under the GNU General Public License v3.0.

"""

wordlist = [x.rstrip('\n') for x in open('source.txt')]

def dedup(x):
  return list(dict.fromkeys(x))

list_lower = [x.lower() for x in wordlist]
for x in list_lower:
    wordlist.append(x)
wordlist = dedup(wordlist)

list_cap = [x.capitalize() for x in wordlist]
for x in list_cap:
    wordlist.append(x)
wordlist = dedup(wordlist)

list_converta = [x.replace("a", "@") for x in wordlist]
for x in list_converta:
    wordlist.append(x)
wordlist = dedup(wordlist)

list_convert1a = [x.replace("a", "@", 1) for x in wordlist]
for x in list_convert1a:
    wordlist.append(x)
wordlist = dedup(wordlist)

list_convert2a = [x.replace("a", "@", 2) for x in wordlist]
for x in list_convert2a:
    wordlist.append(x)
wordlist = dedup(wordlist)

list_convert3a = [x.replace("a", "@", 3) for x in wordlist]
for x in list_convert3a:
    wordlist.append(x)
wordlist = dedup(wordlist)

list_converte = [x.replace("e", "3") for x in wordlist]
for x in list_converte:
    wordlist.append(x)
wordlist = dedup(wordlist)

list_convert1e = [x.replace("e", "3", 1) for x in wordlist]
for x in list_convert1e:
    wordlist.append(x)
wordlist = dedup(wordlist)

list_convert2e = [x.replace("e", "3", 2) for x in wordlist]
for x in list_convert2e:
    wordlist.append(x)
wordlist = dedup(wordlist)

list_convert3e = [x.replace("e", "3", 3) for x in wordlist]
for x in list_convert3e:
    wordlist.append(x)
wordlist = dedup(wordlist)

list_converto = [x.replace("o", "0") for x in wordlist]
for x in list_converto:
    wordlist.append(x)
wordlist = dedup(wordlist)

list_convert1o = [x.replace("o", "0", 1) for x in wordlist]
for x in list_convert1o:
    wordlist.append(x)
wordlist = dedup(wordlist)

list_convert2o = [x.replace("o", "0", 2) for x in wordlist]
for x in list_convert2o:
    wordlist.append(x)
wordlist = dedup(wordlist)

list_convert3o = [x.replace("o", "0", 3) for x in wordlist]
for x in list_convert3o:
    wordlist.append(x)
wordlist = dedup(wordlist)

list_swap = [x.swapcase() for x in wordlist]
for x in list_swap:
    wordlist.append(x)
wordlist = dedup(wordlist)

list_spaceless = [x.replace(" ", "") for x in wordlist]
for x in list_spaceless:
    wordlist.append(x)
dictionary = dedup(wordlist)
dictionary.sort()

output = open('dictionary.txt','w')

for x in dictionary:
    print(x, file=output)
output.close()
