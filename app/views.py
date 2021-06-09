from flask import render_template
from .request import get_news, get_everything
from app import app

# Views
@app.route('/')
def index():
    
    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    data = get_news()
    return render_template('index.html', data = data)

@app.route('/everything')
def index_func():
    
    edata = get_everything()
    return render_template('everything.html', edata = edata)