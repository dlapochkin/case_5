import urllib.request
url = 'https://www.nfl.com/players/bryce-petty/stats/'
f = urllib.request.urlopen(url)
s = f.read()
text = str(s)
print(text)