
import urllib.request
with open('input.txt') as f_in:
    for line in f_in:
        print(line)
        f = urllib.request.urlopen(line)
        s = f.read()
        text = str(s)
        part_name = text.find("nfl-c-player-header__title")
        name = text[text.find('>',part_name)+1:text.find('</h1',part_name)]
        with open('output.txt','w') as f_out:
            print(name, file=f_out)
            part_att = text.find("passingAttempts")
            att = text[text.find('>',part_att)+1:text.find('</th>',part_att)]
            u=''
            for l in att:
                if l.isdigit():
                    u+=l
                print(u, file=f_out)
