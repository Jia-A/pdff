from flask import Flask, render_template, url_for
app = Flask(__name__)
print(__name__)


@app.route('/')
def Home():
    return render_template('100.html')

@app.route('/mainpage')
def Mainpage1():
    return render_template('200.html') 


