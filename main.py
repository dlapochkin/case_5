import urllib.request
with open('output.txt','w') as f_out:
    with open('input.txt') as f_in:
        for line in f_in:
            print(line)
            f = urllib.request.urlopen(line)
            s = f.read()
            text = str(s)
            part_name = text.find("nfl-c-player-header__title")
            name = text[text.find('>',part_name)+1:text.find('</h1',part_name)]
            print(name)
            print(name, file=f_out)

            part= text[text.find("passingAttempts")+1:text.find("passingFirstdowns")]
            while '>' in part:
                att = part [part.find('>')+1:part.find('</th>')]
                u= att.replace('\\','')
                u=u.replace('n','')
                print(u, file=f_out)
                part=part[part.find('</th>')+5:]
