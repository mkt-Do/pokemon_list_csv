import requests
from bs4 import BeautifulSoup

target_url = 'http://blog.game-de.com/pm-usum/usum-allstatus/'
r = requests.get(target_url)

soup = BeautifulSoup(r.text, 'lxml')

for tr in soup.find_all('tr'):
    s = ''
    for td in tr.find_all('td'):
        if td.text.count(' '):
            arr = td.text.split(' ')
            for i,a in enumerate(arr):
                if a.count('(') and i != 2:
                    arr.insert(i, '')
            if len(arr) != 3:
                while len(arr) != 3:
                    arr.append('')
            for a in arr:
                s += a.replace('(', '').replace(')', '') + ','
        elif td.find('div'):
            arr = []
            for div in td.find_all('div'):
                arr.append(div.text)
            if len(arr) != 2:
                arr.append('')
            for a in arr:
                s += a + ','
        else:
            s += td.text + ','
    txt = s[:-1]
    if txt.count(',') == 11:
        txtarr = txt.split(',')
        txtarr.insert(5, '')
        txtarr.insert(5, '')
        tt = ''
        for t in txtarr:
            tt += t + ','
        print(tt[:-1])
    else:
        print(txt)
