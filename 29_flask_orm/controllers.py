from flask import url_for, redirect, \
                    render_template, request

from app import app
from models import Blog

user_list = [
    {
        'name': 'John Doe',
        'email': 'user1@mail.com',
        'password': '1234',
    },
    {
        'name': 'user 2 name',
        'email': 'user2@mail.com',
        'password': '12345'
    },
    {
        'name': 'user 3 name',
        'email': 'user3@mail.com',
        'password': '123456'
    },
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home-redirection/')
def home_redirection():
    return redirect(url_for('index'))


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request.form, '-----------------')
        email = request.form['email']
        password = request.form['password']
        for i in user_list:
            if i['email'] == email:
                if i["password"] == password:
                    return redirect(url_for('profile', name=i['name']))
                

    return render_template('login.html')


@app.route('/profile/<name>')
def profile(name):
    return render_template('profile.html', name=name)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        user = {}
        user['name'] = name
        user['email'] = email
        user['password'] = password

        user_list.append(user)

        return redirect(url_for('login'))
    
    return render_template('register.html')


@app.route('/blogs/')
def blogs():
    blogs = Blog.query.filter_by(status=True)
    context = {
        "blogs": blogs
    }
    return render_template('blogs.html', **context)
