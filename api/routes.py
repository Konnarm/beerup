from flask import render_template
from meetUPbeerUP import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Meet UP beer UP!')
