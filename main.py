import urllib.request
url = 'https://www.nfl.com/players/bryce-petty/stats/'
f = urllib.request.urlopen(url)
s = f.read()
text = str(s)
part_name = text.find("nfl-c-player-header__title")
name = text[text.find('>',part_name)+1:text.find('</h1',part_name)]
print(name)
url = 'https://www.nfl.com/players/bryce-petty/stats/'
f = urllib.request.urlopen(url)
s = f.read()
text = str(s)
part_name = text.find("nfl-c-player-header__title")
name = text[text.find('>',part_name)+1:text.find('</h1',part_name)]
print(name)