"""Case-study #4 Парсинг web-страниц
Разработчики:
Кривошапова Д.Е (70%)
Лапочкин Д.А (15%)
Кузнецов А.Д (20%)
"""
import urllib.request
with open('output.txt','w') as f_out:
    with open('input.txt') as f_in:
        for line in f_in:
            f = urllib.request.urlopen(line)
            s = f.read()
            text = str(s)
            part_name = text.find("nfl-c-player-header__title")
            name = text[text.find('>',part_name)+1:text.find('</h1',part_name)]
            part_rt = text.find('passingPasserRating')
            rt = text[text.find('>', part_rt) + 1:text.find('</th>', part_rt)]
            nrt = rt.replace('\\', '')
            rt = nrt.replace('n', '')
            rt=rt.strip()
            nrt=float(rt)
            part= text[text.find("passingAttempts")+1:text.find("passingFirstdowns")]
            n=[]
            while '>' in part:
                att = part [part.find('>')+1:part.find('</th>')]
                u= att.replace('\\','')
                u=u.replace('n','')
                n.append(u.strip())
                part=part[part.find('</th>')+5:]
            print('{:20s}{:<7s}{:<7s}{:<7s}{:<7s}{:<7s}{:<7.2f}'.format(name, n[1], n[0], n[3], n[6], n[7],nrt),file=f_out)