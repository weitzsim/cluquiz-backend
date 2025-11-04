from flask import Flask
from flask import url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/questions/<int:count>')
def show_questions(count):
    return f'<p>Hello, World! wie viel questioins? -> {count}</p>'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/login')
def login():
    return "<p>Hello, login!</p>"

@app.post('/post')
def login_post():
    return do_the_login()

@app.route('/logintwoway', methods=['GET', 'POST'])
def logintwoway():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

with app.test_request_context():
    print(url_for('show_questions', count='3'))


