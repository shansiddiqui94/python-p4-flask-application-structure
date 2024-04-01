User
#!/usr/bin/env python3
# you need to be in the correct file if you are to run the page
from flask import Flask

app = Flask(__name__)

@app.route("/") #default route
def index():
    return '<h1>Welcome to my page!</h1>'

@app.route('/<username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)