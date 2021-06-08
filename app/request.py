from instance import config
from newsapi import NewsApiClient

my_api_key = config.api_key

def get_news():

    newsapi = NewsApiClient(my_api_key)
    topheadlines = newsapi.get_top_headlines(sources="al-jazeera-english")

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    url = []
    pub =[]

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
        pub.append(myarticles['publishedAt'])
    
        
    mylist = zip(desc, news, img, pub,url)

    return mylist
