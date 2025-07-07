"""
News Controller.

This Service class is generated from a template.
"""

import os
from abc import abstractmethod
from typing import List, Dict, Any, Optional
from fletx.core import FletXService
from newsapi import NewsApiClient
from newsdataapi import NewsDataApiClient

from app.models import Article, ArticleSource


####
##      BASE NEWS PROVIDER 
####
class BaseProvider:
    """Base class for all News APIs Providers"""
    
    client = None
    max_per_page: int = 10

    @abstractmethod
    def parse_news(self,news:List[Dict[str,Any]]):
        """Parse News List into Article List"""

    @abstractmethod
    def get_popular_news(self,category:str):
        """Get popular news from Provider"""

    @abstractmethod
    def get_category_news(self):
        """Get a given category news from Provider"""


####
##      NEWS API PROVIDER (newsapi.org)
#####
class NewsApiProvider(BaseProvider):
    """Newsapi.org Provider"""

    client = NewsApiClient(api_key = os.environ.get('NEWS_APIKEY'))

    def parse_news(self, news: List[Dict[str,Any]]):
        """Parse a list of news into article objects"""

        articles = [
            Article(
                source = ArticleSource(
                    id = article['source']['id'],
                    name = article['source']['name']
                ),
                title = article['title'],
                author = article['author'],
                description = article['description'],
                url = article['url'],
                url_to_image = article['urlToImage'],
                published_at = article['publishedAt'],
                content = article['content']
            )
            for article in news
        ]
        # print('\n\n\nNEWS: ',news,'\n\n\n')

        return articles
    
    def get_popular_news(
        self,
        # category: str ,
        search: str = 'pycon 2025',
    ):
        """Get Popular news from NewsAPI."""

        news = self.client.get_everything(
            q = search,
            # qintitle = 'python programming',
            # sources = 'bbc-news,the-verge,medium,hacker-news',
            # category = 'business',
            sort_by = 'popularity',
            page_size = self.max_per_page
        )

        return self.parse_news(news['articles'])
    
    def get_category_news(
        self,
        search: Optional[str] = None,
        category: Optional[str] = None,
        page: int = 1
    ):
        """Get News Sources from NEWS API"""

        # We'll Just use id and name, so we can use article source model.
        news = self.client.get_top_headlines(
            q = search,
            # qintitle = '',
            category = category or 'general',    # All by default
            # sort_by = 'popularyty',
            page_size = self.max_per_page,
            page = page
        )

        return self.parse_news(news['articles'])
    

####
##      NEWS DATA API PROVIDER (newsdata.io)
#####
class NewsDataApiProvider(BaseProvider):
    """Newsdata.io Provider"""

    def __init__(self):
        self.client = NewsDataApiClient(
            apikey = os.environ.get('NEWS_DATA_APIKEY')
        )

    def parse_news(self, news):

        articles = [
            Article(
                source = ArticleSource(
                    id = article['source_id'],
                    name = article['source_name']
                ),
                title = article['title'],
                description = article['description'],
                url = article['link'],
                url_to_image = article['image_url'],
                content = article['content'],
                published_at = article['pubDate'],
                author = article['creator'] or 'Unknown'

            )
            for article in news
        ]
        print(articles)
        return articles

    def get_category_news(
        self, 
        category: str = '',
        search: str = ''
    ):
        """Get a given category news from NeasData.io"""

        news = self.client.news_api(
            q = search,
            category = category,
            image = True,
            max_result = self.max_per_page,
            removeduplicate = True
        )

        return self.parse_news(news['results'])
    
    def get_popular_news(
        self,
        search: str = ''
    ):
        """Get Popular news from Provider"""
        return self.get_category_news(category = 'general')


####
##      NEWS SERVICE
#####
class NewsService(FletXService):
    """News Service"""

    def __init__(self, *args, **kwargs):
        self.base_url = ""
        self.newsapi = NewsApiClient(api_key = os.environ.get('NEWS_APIKEY'))

        # Init base class
        super().__init__(**kwargs)

    def on_start(self):
        """Do stuf here on NewsService start"""
        pass
    
    def on_stop(self):
        """Do stuf here on NewsService stop"""
        pass

    def get_provider(self, name:str = '') -> BaseProvider:
        """Get API Provider by name"""

        providers = {
            '': NewsApiProvider(),
            'newsapi.com': NewsApiProvider(),
            'nwasdata.io': NewsDataApiProvider()
        }

        return providers.get(name)

    def get_popular_news(
        self,
        category: str ,
        search: str = 'pycon 2025',
        limit: int = 10,
    ):
        """Get Popular news from NewsAPI."""

        return self.get_provider().get_popular_news(
            search = search,
        )
    
    def get_category_news(
        self,
        search: Optional[str] = None,
        category: Optional[str] = None,
        limit: int = 10,
        page: int = 1
    ):
        """Get News Sources from NEWS API"""

        return self.get_popular_news(
            search = search,
            category = category,
        )
