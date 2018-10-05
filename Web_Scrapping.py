import re
import urllib.request

search = input("Enter the search text your looking for : ")

url = "https://en.wikipedia.org/wiki/"+ search

data = urllib.request.urlopen(url).read()
formatdata = data.decode("utf-8")


text = re.search('div id="mw-content-text"|div|p[1]', formatdata)

start = text.end()
end = start + 300

# text = re.search("</div>", formatdata)
# end = text.start() - 2

newString = formatdata[start:end]

final = newString[0:end]

print(final)