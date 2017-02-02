import pyperclip
import re

# regex for http or https URLs
# http://some+.-_thing/ or https://some.-_thing/ or http://some+_-thing
# https://some+_-thing or http://some+-thing/some+-_thing/
httpRegexp = re.compile(r'''
(
http(s)?://    # http or https
[a-zA-Z0-9.+-]+    # (some+.-thing) one or more
/?          # / zero or 1
#([a-zA-Z0-9.+-]+(/)?)*     # (some+.-thing/ (slash optional)) 0 or more
)
''', re.VERBOSE)

# Copy the source from clipboard
text = pyperclip.paste()

# TODO: Clean the list and format it
mo = httpRegexp.findall(text)
urls = []
for url in mo:
    urls.append(url[0])

showURLs = '\n'.join(urls)

# TODO: Paste the formatted list into the clipboard
print(str(len(urls)) + ' URLs found')

pyperclip.copy(showURLs)
