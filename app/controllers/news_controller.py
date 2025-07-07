"""
News Controller.

This controller class is generated from a template.

🛠️ Customization Guide:
- You can rename or extend this class as needed.
  → Example: Inherit from a different base if you use a custom controller class.
- Add your own reactive attributes using types like `RxInt`, `RxStr`, `RxBool`, etc.
- Implement methods to handle business logic, side effects, or custom events.
- Controllers can be injected into components or apps using dependency injection or manual wiring.
"""

from typing import List, Optional
from fletx import FletX
from fletx.core import (
    FletXController, RxInt, RxBool, RxList
)

from app.models import Article, ArticleSource
from app.services import NewsService

class NewsController(FletXController):
    """News Controller"""

    def __init__(self):
        self.search_enabled: RxBool = RxBool(False)
        self.popular_news: RxList = RxList([])
        self.categories: RxList = RxList([])
        self.categories: List[str] = [
            'general','business', 'entertainment',
            'health', 'science', 'sports', 'technology'
        ]

        # Services
        self.news_service: NewsService = FletX.put(NewsService(),'news')
        super().__init__()

    def on_initialized(self):
        """Hook called when initializing controller"""
        self.get_popular_news()

    def fetch_all_category_news(self):
        """Fetch news for each category"""
        for category in self.categories:
            self.get_category_news(category = category)

    def on_ready(self):
        """Hook called when the controller is ready"""
        print("NewsController is READY!!!")
    
    def on_disposed(self):
        """Hook called when disposing controller"""
        print("NewsController is disposing")

    def get_popular_news(self):
        """Get Popular news from API"""

        # Change state
        self.set_loading(True)
        
        try:
            # Get News
            self.popular_news.value = self.news_service.get_popular_news()
            # print(self.popular_news.value)
        
        # Handle Exceptions
        except Exception as e:
            print(f'Error when fetching popular news: {e}')
            self.set_error(str(e))

        # Change State
        finally: 
            self.set_loading(False)

    def get_category_news(self, category: Optional[str] = None):
        """Get a given category news fom service."""

        # Change State
        self.set_loading(True)

        try:
            print(f'Fetching {category}.......................................')
            # Get The news
            news = self.news_service.get_category_news(
                category = category,
            )
            print('\n\n\n\n\n',news,'\n\n\n\n\n')
            # Add Category news to Controllers's global context.
            # So we can access it anywhere in our application via any controller
            self.set_global_context(
                f'{category if category else 'all'}_news',
                news
            )

        # Exception occures
        except Exception as e:
            print(f'Error when fetching category news: {e}')
            self.set_error(str(e))

        # Change State
        finally: 
            self.set_loading(False)
    