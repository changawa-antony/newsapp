from flask import render_template
from app import app
from .request import get_news

# Views
@app.route('/')
def index():
    
    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    latest_news = get_news()
    return render_template('index.html',latest_news=latest_news)