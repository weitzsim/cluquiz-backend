import os

from flask import Flask
from flask import url_for
from . import db
from . import auth

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    app.register_blueprint(auth.bp)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

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


    return app
