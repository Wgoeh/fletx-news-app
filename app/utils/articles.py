import random
from app.models import Article, ArticleSource

IMAGES = [
    'https://www.washingtonpost.com/wp-apps/imrs.php?src=https://arc-anglerfish-washpost-prod-washpost.s3.amazonaws.com/public/EMOMTWWBKZZHAKCF3N3MQHAQF4_size-normalized.jpg',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRe2IHO_n34-10RlM3AwvxLPtQUYmwc3yRLTggAXw9Kt4ZlLTsmHslqsvmtggAmnYF4po0&usqp=CAU',
    'https://thumbs.dreamstime.com/b/news-newspapers-folded-stacked-word-wooden-block-puzzle-dice-concept-newspaper-media-press-release-42301371.jpg',
    'https://dailynews.co.tz/wp-content/uploads/2025/05/artificial-intelligence-new-technology-science-futuristic-abstract-human-brain-ai-technology-cpu-central-processor-unit-chipset-big-data-machine-learning-cyber-mind-domination-generative-ai-scaled-1-780x470.jpg',
    'https://elroy.twit.tv/sites/default/files/styles/twit_slideshow_600x450/public/images/shows/tech_news_today/hero/tnt_megan_jason.jpg?h=34bbd072',
    'https://files.realpython.com/media/Monthly-Python-News_Red_Watermarked.c82fffdbc32e.jpg',
    'https://files.realpython.com/media/Interacting-with-Python_Watermarked.0007ad8964b8.jpg',
    'https://files.realpython.com/media/Python-3.12-Cool-New-Features_Watermarked.608b58320f27.jpg',
    'https://files.realpython.com/media/Class-Concepts-Object-Oriented-Programming-in-Python_Watermarked.6cf327c51434.jpg',
    'https://miro.medium.com/v2/resize:fit:2000/0*c1zS0RHWXtJaiMaF.png',
    'https://images.squarespace-cdn.com/content/v1/627169b455eacf0a6cae7140/1749040420225-1CXTGNAJ55LQGFMX33TW/Screenshot+2025-06-04+at+11.25.22.jpg',
    'https://i.ytimg.com/vi/6Tj8_iKqh_k/maxresdefault.jpg',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQF8673vWQYTAsGCINeA4uiinVt-TrR88QHig&s',
    'https://i.ytimg.com/vi/JJCjAUmNXBs/maxresdefault.jpg',
    'https://miro.medium.com/v2/resize:fit:1400/1*qK7DpsXbt-JCwttRMeOaNQ.png',
    'https://i.ytimg.com/vi/HSiTkOPZmtc/hqdefault.jpg',
    'https://cdn.dribbble.com/userupload/43273034/file/original-45fe1a1f6cd7427c3f2c6d536d81ff0f.jpg',
    'https://cdn.dribbble.com/userupload/15656345/file/original-e8705080f81f788f96d99e277034342f.jpg',
    'https://cdn.dribbble.com/userupload/43098102/file/original-52c1764e44918b9a54d70d982f70b9cb.jpg',
    'https://i.pinimg.com/736x/fe/f7/b3/fef7b3cbaeb59afc974ab04dd20741e6.jpg',
    'https://i.pinimg.com/736x/cf/12/b7/cf12b7007e8f69025dc5c389fc6a7cf4.jpg'
    'https://i.pinimg.com/736x/ac/c3/ba/acc3ba11c77639e59fbd120d451e0105.jpg',
    'https://i.pinimg.com/736x/10/d7/63/10d763bdddad5203a6afddcaf8fb114a.jpg',
    'https://i.pinimg.com/736x/92/e4/f4/92e4f49ab6efe52f10471c5b9f4d56c9.jpg',
    'https://alldotpy.github.io/FletX/assets/logo/fletx_t.png'
]

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

def random_img():
    """Generate article with random image"""

    return random.choice(IMAGES)

def get_fake_articles(limit: int = 10):

    return [
        Article(
            source = ArticleSource(
                id = 'bbc',
                name = 'bbc news'
            ),
            author = 'John doe',
            title = "We're building news app with flet and FletX",
            description = 'A FletX showcase creating a sample News App',
            url = 'https://alldotpy.github.io/FletX/',
            url_to_image = random_img(),
            published_at = '',
            content = DESC,
        )
        for i in range(limit)
    ]