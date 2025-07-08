"""
Onboarding Controller.

This Page class is generated from a template.
"""

from flet import *
from fletx import FletX
from fletx.core import FletXPage
from fletx.navigation import navigate
# from fletx.utils import run_async, get_event_loop

# Import your modules here...
from app.utils import (
    dark_gradient, show_loader, show_snackbar
)
from app.controllers import NewsController


class OnboardingPage(FletXPage):
    """Onboarding Page"""

    def __init__(self):
        self.newsController: NewsController = FletX.put(
            NewsController(), tag = 'news_ctrl'
        )
        super().__init__(
            padding = 0,
            # bgcolor = Colors.BLACK
        )

        # ...

    def on_init(self):
        """Hook called when OnboardingPage in initialized"""

        # Watch controller's loading state and 
        # show loader when it changes.
        self.watch(
            self.newsController._is_loading,
            callback = lambda: show_loader(
                controller = self.newsController,
                page = self.page
            ),
            immediate = True
        )
        
        # Fetch news for all gategories
        self.newsController.fetch_all_category_news()
        

    def on_destroy(self):
        """Hook called when OnboardingPage will be unmounted."""

        print("OnboardingPage is destroyed")

    def build(self)-> Control:
        """Method that build OnboardingPage content"""

        return Stack(
            expand = True,
            # alignment = MainAxisAlignment.CENTER,
            # horizontal_alignment = CrossAxisAlignment.CENTER,
            controls = [
                Container(
                    expand = True,

                    content = Image(
                        src = "images/trump.jpg",
                        # width = 200,
                        # height = 200,
                        fit = ImageFit.COVER
                    ),
                ),
                Container(
                    expand = True,
                    width = self.width,
                    gradient = dark_gradient,
                    padding = 20,

                    content = Column(
                        expand = True,
                        alignment = MainAxisAlignment.END,
                        horizontal_alignment = CrossAxisAlignment.CENTER,
                        controls = [
                            Container(expand=True),
                            Text("Discover Breaking News", size=28, weight=FontWeight.BOLD),
                            Text(
                                (
                                    "Use the unofficial Python client library to integrate"
                                    " News API into your Python application without having "
                                    "to make HTTP requests directly."
                                ), 
                                text_align = TextAlign.CENTER,
                                size=14
                            ),
                            # Text("Enjoy your stay!", size=16),

                            Container(height=20),  # Spacer

                            # ICON BUTTON
                            Container(
                                width = 65,
                                height = 65,
                                ink = True,
                                alignment = alignment.center,
                                bgcolor = Colors.PRIMARY_CONTAINER,
                                border_radius = 32,
                                on_click = (
                                    lambda e: navigate('/') 
                                    if not self.newsController._is_loading.value 
                                    else show_snackbar(
                                        page = self.page,
                                        title = 'Please wait a bit more',
                                        message = 'Please wait until news data is loaded!',
                                        type = 'info'
                                    )
                                ),

                                content = Icon(
                                    Icons.ARROW_FORWARD,
                                    color = Colors.ON_PRIMARY_CONTAINER,
                                    size = 28,
                                )
                            ),
                            Container(height=50),  # Spacer
                        ]
                    )
                ),
            ]
        )