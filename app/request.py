from app import app
import urllib.request,json
from .models import news

# Getting api key
api_key = app.config['NEWS_API_KEY']
News = news.News

# Getting the news
base_url = app.config["NEWS_API_BASE_URL"]

def get_news():
    '''
    Getting json response to the API
    '''
    get_news_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read().decode("utf8", 'ignore')
        get_news_response = json.loads(get_news_data)

        news_results = get_news_response

    return news_results


def process_results(news_list):
    '''
    Transforms the results to an object
    '''
    news_results = []
    for news_item in news_list:
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        publishedAt = news_item.get('publishedAt')

        news_object = News(author,title,description,url,publishedAt)
        news_results.append(news_object)

    return news_results