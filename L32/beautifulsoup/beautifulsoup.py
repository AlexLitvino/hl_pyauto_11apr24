# https://www.crummy.com/software/BeautifulSoup/bs4/doc.ru/bs4ru.html#id11
# https://beautiful-soup-4.readthedocs.io/


from bs4 import BeautifulSoup

with open('Bill(law)-Wikipedia.html') as f:
    soup = BeautifulSoup(f, "html.parser")

# h2 = soup.findAll('h2')
# for header in h2:
#     print(header.text)

divs = soup.findAll('div')
for div in divs[:10]:
    print(div.attrs)
