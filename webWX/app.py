from flask import Flask,render_template,session,jsonify
from bs4 import BeautifulSoup
import re,time,requests

app = Flask(__name__)
app.secret_key = 'wechat'

def xml_parse(text):
    ret = {}
    soup = BeautifulSoup(text,'html.parser')
    tag_lsit = soup.find(name='error').find_all()
    for tag in tag_lsit:
        ret[tag.name] = tag.text
    return ret



@app.route('/login')
def login():
    ctime = int(time.time() * 1000)
    #https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb&redirect_uri=https%3A%2F%2Fwx.qq.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&fun=new&lang=zh_CN&_=
    qcode_url = 'https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb&redirect_uri=https%3A%2F%2Fwx.qq.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&fun=new&lang=zh_CN&_={0}'.format(ctime)
    req = requests.get(
        url = qcode_url,
    )

    qcode = re.findall('uuid = "(.*)";',req.text)[0]
    session['qcode'] = qcode
    return render_template('login.html',qcode=qcode)

@app.route('/check/login')
def check_login():
    response = {'code':408}
    ctime = int(time.time() * 1000)
    qcode = session['qcode']
    check_login_url = 'https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid={0}&tip=1&r=12601156&_={1}'.format(qcode,ctime)

    code = requests.get(url=check_login_url)
    if 'window.code=408' in code.text:
        pass
    elif 'window.code=201' in code.text:
        response['code'] = 201
        response['avatar'] = re.findall("window.code=201;window.userAvatar = '(.*)';",code.text)[0]
    elif 'window.code=200' in code.text:
        response['code'] = 200
        #拿凭证
        redirect_uri = re.findall('window.redirect_uri="(.*)";', code.text)[0] + '&fun=new&version=v2'
        response['redirect_uri']=redirect_uri
        ru = requests.get(url=redirect_uri)
        print(ru.text)
        ticket_dict = xml_parse(ru.text)
        session['ticket_dict'] = ticket_dict
    return jsonify(response)

@app.route('/index')
def index():


    return render_template('index.html')

if __name__ == '__main__':
    app.run()
