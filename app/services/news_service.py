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
from app.utils import with_random_img

DESC = """
# ✨ Welcome to FletX

**FletX** is a lightweight, modular, and reactive architectural framework built on top of [Flet](https://flet.dev), designed to help you build scalable Python UI applications with clean code, structured layers, and modern development patterns.

---

## What is FletX?

Inspired by frameworks like **GetX** in the Flutter ecosystem, **FletX** introduces powerful architectural patterns to Flet:

- ✅ **Reactive state management**
- ✅ **Modular routing system** with dynamic parameters and guards
- ✅ **Controllers and services** to separate logic from UI
- ✅ **Global and local dependency injection**
- ✅ **Lifecycle hooks** for pages and the app
- ✅ **Unified configuration with fluent API**
- ✅ **Built-in support for asynchronous programming**

---

## 🧠 Philosophy

FletX is built on 3 core principles:

1. **Simplicity** — Focus on code clarity and maintainability  
2. **Modularity** — Encourage component-based structure and reusable logic  
3. **Flexibility** — Allow full control over your app flow, while staying non-intrusive  

*FletX is not a UI library. It doesn’t reinvent Flet’s widgets — it empowers you to use them better by providing a powerful and extensible application layer.*

---

## ⚡ Quick Example

```python
import flet as ft

from fletx.app import FletXApp
from fletx.core import (
    FletXPage, FletXController, RxInt, RxStr
)
from fletx.navigation import router_config
from fletx.decorators import (
    simple_reactive
)


class CounterController(FletXController):

    def __init__(self):
        self.count = RxInt(0)
        super().__init__()


@simple_reactive(bindings={'value': 'text'})
class MyReactiveText(ft.Text):

    def __init__(self, rx_text: RxStr, **kwargs):
        self.text: RxStr = rx_text
        super().__init__(**kwargs)


class CounterPage(FletXPage):
    ctrl = CounterController()

    def build(self):
        return ft.Column(
            controls=[
                MyReactiveText(rx_text=self.ctrl.count, size=200, weight="bold"),
                ft.ElevatedButton(
                    "Increment",
                    on_click=lambda e: self.ctrl.count.increment()
                )
            ]
        )


def main():
    router_config.add_route(path='/', component=CounterPage)
    app = FletXApp(
        title="My Counter",
        initial_route="/",
        debug=True
    ).with_window_size(400, 600).with_theme(
        ft.Theme(color_scheme_seed=ft.Colors.BLUE)
    )

    app.run()


if __name__ == "__main__":
    main()
```


---

## 📌 Usefull Links

* [GitHub Repository](https://github.com/AllDotPy/FletX) :star:
* [PyPI Package](https://pypi.org/project/FletXr/)
* [Join the Community on Discord](https://discord.gg/GRez7BTZVy)
* [License](LICENSE)

---

Made with ❤️ by [AllDotPy](https://alldotpy.com)

"""

ARTICLE = Article(
    source = ArticleSource(
        id = 'bbc',
        name = 'bbc news'
    ),
    author = 'John doe',
    title = "We're building news app with flet and FletX",
    description = 'A FletX showcase creating a sample News App',
    url = 'https://alldotpy.github.io/FletX/',
    url_to_image = 'https://alldotpy.github.io/FletX/assets/logo/fletx_t.png',
    published_at = '',
    content = DESC,
    # (
    #     'we made a sample news app using the GetX-like micro-framework for flet. '
    #     'This project shows how to use flet with fletx create reactive apps, '
    #     'it shows also how to usee some fletx compnents like Controllers, Pages, '
    #     'Services, Reactive States with RX[T] variants, widget decorators and more...'
    # )
)


####
##      NEWS SERVICE
#####
class NewsService(FletXService):
    """News Service"""

    def __init__(self, test_mode: bool = False, *args, **kwargs):
        self.base_url = ""
        self.max_per_page: int = 20
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
            return [with_random_img(ARTICLE) for i in range(self.max_per_page)]

        news = self.newsapi.get_everything(
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
        page: int = 20
    ):
        """Get News Sources from NEWS API"""

        if self.test_mode:
            return [builder(ARTICLE) for builder in [ lambda art: with_random_img(art) for i in range(self.max_per_page)]]

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
