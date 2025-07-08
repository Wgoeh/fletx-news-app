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
from app.utils import get_fake_articles


####
##      NEWS SERVICE
#####
class NewsService(FletXService):
    """News Service"""

    def __init__(self, test_mode: bool = False, *args, **kwargs):
        self.base_url = ""
        self.max_per_page: int = 25
        self.test_mode: bool = test_mode
        self.newsapi = NewsApiClient(api_key = os.environ.get('NEWS_APIKEY'))

        # Init base class
        super().__init__(**kwargs)

    def on_start(self):
        """Do stuf here on NewsService start"""
        pass
    
    def on_stop(self):
        """Do stuf here on NewsService stop"""
        pass

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

        if self.test_mode:
            return get_fake_articles(self.max_per_page)

        try:
            news = self.newsapi.get_everything(
                q = search,
                # qintitle = 'python programming',
                # sources = 'bbc-news,the-verge,medium,hacker-news',
                # category = 'business',
                sort_by = 'popularity',
                page_size = self.max_per_page
            )

            return self.parse_news(news['articles'])
        
        # Return test articles else
        except Exception as e:
            print(e)
            return get_fake_articles(self.max_per_page)
    
    def get_category_news(
        self,
        search: Optional[str] = None,
        category: Optional[str] = None,
        page: int = 20
    ):
        """Get News Sources from NEWS API"""

        if self.test_mode:
            return get_fake_articles(self.max_per_page)

        try:
            # We'll Just use id and name, so we can use article source model.
            news = self.newsapi.get_top_headlines(
                q = search,
                # qintitle = '',
                category = category if category else 'general',    # All by default
                # sort_by = 'popularyty',
                page_size = self.max_per_page,
                page = page
            )

            return self.parse_news(news['articles'])
        
        # Return test articles else
        except Exception as e:
            print(e)
            return get_fake_articles(self.max_per_page)

