from flask import Flask,render_template,request,jsonify,session
import queue,uuid

app = Flask(__name__)
app.secret_key = 'hhhhhhh'

USERS={
    '1':{'name':'酒窝','count':4},
    '2':{'name':'琰琰','count':2},
    '3':{'name':'丹丹','count':0},
}

QUEUE_DICT ={

}


@app.route('/user/list')
def user_list():
    user_uuid = str(uuid.uuid4())
    QUEUE_DICT[user_uuid] = queue.Queue()
    session['current_user_uuid'] = user_uuid

    return render_template('show.html',users=USERS)

@app.route('/vote',methods=['POST',])
def vote():

    uid = request.form.get('uid')
    USERS[uid]['count'] += 1

    for q in QUEUE_DICT.values():
        q.put(USERS)


    return '投票成功！'

@app.route('/get/vote',methods=['GET'])
def get_vote():
    ret = {'status':True,'data':None}
    user_uuid = session['current_user_uuid']
    q = QUEUE_DICT[user_uuid]
    try:
        users = q.get(timeout=5)
        ret['data'] = USERS
    except queue.Empty:
        ret['status'] = False

    return jsonify(ret)


if __name__ == '__main__':
    app.run()
    # app.run(host='192.168.0.105',threaded = True)