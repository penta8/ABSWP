#! /usr/bin/env python3
#  regexSearch.py: the user enter a regular expression without quotes
#                  and look for in the same directory to see if there
#                  are txt files that have text to match the regular
#                  expression

import re
import os


def binaryFile(f):
    with open(f, 'rb') as fi:
        binary = b'\x00' in fi.read()
    return binary


def getBinFiles(dir):
    textFiles = []
    for f in os.listdir('.'):
        if os.path.isfile(f) and not binaryFile(f):
            textFiles.append(f)
    return textFiles


# user enter a regular expression and assign it to userRegexp
def main():
    usInput = input('Enter a valid regular expression with no quotes: ')
    userRegexp = re.compile('(' + usInput + ')')

    # look for text files in the current directory
    textFiles = getBinFiles('.')

    # for each text file look for userRegexp if it is found print the
    #       line and the userRegexp found
    for f in textFiles:
        with open(f) as fi:
            line = fi.readline()
            while line != '':
                found = userRegexp.search(line)
                if found:
                    print()
                    print('PATTERN FOUND in file: ' + f)
                    print('Line: %s' % line.strip('\n'))
                    print('Pattern: %s' % found.group())
                line = fi.readline()


if __name__ == '__main__':
    main()
