import re


def stripRegex(string, char=' '):
    '''
    in: string
    out: remove spaces from the end and beginning
    of string, if argument char provided, remove
    char from the end and beginning of string
    '''
    startStrip = re.compile(r'^([' + char + '])*')
    endStrip = re.compile(r'([' + char + '])*$')

    # remove char from start and end of string
    string = startStrip.sub('', string)
    return endStrip.sub('', string)
