"""Case-study #4 Парсинг web-страниц
Разработчики:
Иванов А.С., Петров П.С., Сидоров C.H.
""" 
import urllib.request
url = 'https://www.nfl.com/players/bryce-petty/stats/'
f = urllib.request.urlopen(url)
s = f.read()
with open('html.txt', 'w') as out:
  out.write(s)
