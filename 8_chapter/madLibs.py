#! /Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# madLibs.py runs an interactive program where a user select
#            and adjective, noun or verb according to the text
#            it creates a new text file for the user selections
#            it continues increasing the number of file, so the
#            previous files won't be replaced

import os
import re

text = 'The ADJECTIVE panda walked to the NOUN1 and then VERB. ' \
        'A nearby NOUN2 was unaffected by these events.'


# The user is prompted to select a word for an ADJECTIVE, a VERB and 2 NOUNS
#       the user has to enter something otherwise is prompted again.

print(text)

values = {'ADJECTIVE': '', 'NOUN1': '', 'VERB': '', 'NOUN2': ''}

for v in values.keys():
    while values[v] == '':
        values[v] = input('Enter a %s: ' % v)
        if values[v] == '':
            print('Please write something')

# print the new string and save the values to a new file replacing text
# with the gotten values
newText = 'The %s panda walked to the %s and then %s. A nearby %s' \
          ' was unaffected by these events.' \
          % (values['ADJECTIVE'], values['NOUN1'],
             values['VERB'], values['NOUN2'])

# write to a new file in the format sentence#, where # is the number
# of the file, beginning with 1

# get the name of the last file called sentence if there isnt create
# sentence1 otherwise continue with the number
sentRegexp = re.compile(r'sentence(\d{1,})\.txt$')
listFiles = os.listdir('.')

# verify if exist some file called sentence1
sentenceFiles = []
for f in listFiles:
    if sentRegexp.search(f):
        sentenceFiles.append(f)

if sentenceFiles:
    newNumber = int(sentRegexp.search(listFiles[-1]).group(1)) + 1
    newFile = 'sentence' + str(newNumber) + '.txt'
else:
    newFile = 'sentence1.txt'

# Create the new file and append the new sentence created
with open(newFile, 'w') as f:
    f.write(newText)
