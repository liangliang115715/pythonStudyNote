from bs4 import BeautifulSoup

def xml_parse(text):
    ret = {}
    soup = BeautifulSoup(text,'html.parser')
    tag_lsit = soup.find(name='error').find_all()
    for tag in tag_lsit:
        ret[tag.name] = tag.text
    return ret

v = '<error><tag>14</tag></error>'
print(xml_parse(v))