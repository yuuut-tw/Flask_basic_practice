from flask import Flask, request, jsonify, render_template ##FLASK為類別
import poker as p
import series as s
from model import model
from test_controller import test_controller

# 主程式的名稱 => app
app = Flask(__name__, static_url_path='/static_yu', static_folder='./static_yu')
app.register_blueprint(test_controller, url_prefix='/testNamespace')


# 制定接口，透過此接口得到服務
@app.route('/')
def index():
    return "Hello from my Flask!!"

@app.route('/hello/Ben')
def greettoBen():
    return "Hello Ben!!"

@app.route('/hello/<name>')
def greet(name):
    GreetStr = 'Hello {}!'
    return GreetStr.format(name)

@app.route('/hello_get')
def hello_get():
    name = request.args.get('name')
    age = request.args.get('age')
    outputStr = 'Hello {}, You are {} year old'.format(name, age) # http://192.168.43.38:5000/hello_get?name=aram&age=29
    return outputStr # html字串

@app.route('/add/<x>/<y>')
def add(x, y):
    return str(int(x) + int(y)) # 必須是html字串，否則會報錯

@app.route('/hello_post', methods=['GET', 'POST']) # method最一開始以get方式進入頁面，輸入資料後變為post，然後進入if statement
def hello_post():
    method = request.method
    # get 邏輯
    outputStr = '''
    <form action="/hello_post" method="POST">
        <div>
            What's your name?
        </div>    
        <div>
            <input name="username">
        </div>
        <div>
            <button type="submit">Submit</button>
        </div>
    </form>    
    '''
    # 輸入後改變為post方式，進入if statement 運行下面的code
    if method == "POST":
        username = request.form.get("username")
        outputStr += """
        <h3>Hello {}! </h3>
        """.format(username)
    return outputStr

## Controller撰寫
@app.route('/pokerGame/<playerAmount>')
def pokerGame(playerAmount):
    playerAmountInt = int(playerAmount)
    resultJson = p.poker(playerAmountInt) # Json
    return jsonify(resultJson) # Json string

@app.route('/seriesNumber')
def seriesNumber():
    n = int(request.args.get('n'))
    result = str(s.Func(n))
    return result

# jinja2模板
@app.route('/hello_get2')
def hello_get2():
    name = request.args.get('name')
    age = request.args.get('age')
    # render_template return html string
    return render_template('hello_get.html',
                           name=name,
                           age=age)

@app.route('/hello_post2')
def hello_post2():
    method = request.method
    username = request.form.get('username') if method == 'POST' else ''
    return render_template('hello_post.html',
                           method=method,
                           username=username)

@app.route('/poker', methods=['GET', 'POST'])
def poker():
    request_method = request.method
    players = 0
    cards = dict()
    if request_method == 'POST':
        players = int(request.form.get('players'))
        cards = p.poker(players)
    return render_template('poker.html',
                           request_method=request_method,
                           cards=cards)
# controller
@app.route('/show_staff')
def hello_google():
    staff_data = model.getStaff() # model
    column = ['ID', 'Name', 'DeptId', 'Age', 'Gender', 'Salary']
    # view
    return render_template('show_staff.html',
                           staff_data=staff_data,
                           column=column)


# 啟動
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

# note:
# 會在本地端啟動一個網址 http://127.0.0.1:5000/ aka localhost:5000
# debug=True => 程式碼有做任何修改，不須重新啟動，網頁即可自動調整相對應的程式碼