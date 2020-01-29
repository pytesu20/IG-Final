
import requests
import bs4
import webbrowser

def openurl(url):
    webbrowser.get('firefox').open_new_tab(url)

igid = input('enter username : @')

iglink = 'https://www.instagram.com/' + igid


a = iglink

res = requests.get(a)

c = res.text

soup = bs4.BeautifulSoup(res.text, 'html.parser')

abc = soup


txt2 = abc.get_text().split('"')

result = [i for i in txt2 if i.startswith('B')]

start = 'https://www.instagram.com/p/'
end = '/media/?size=l'


b = result
c = []

for everyword in b:
    c.append(start + everyword + end)

print(c)

for everyurl in c:
    openurl(everyurl)
