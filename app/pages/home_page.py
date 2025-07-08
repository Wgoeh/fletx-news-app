"""
Home Controller.

This Page class is generated from a template.
"""

from flet import *
from typing import List
from flet_contrib.shimmer import Shimmer
from fletx import FletX
from fletx.core import FletXPage
from fletx.navigation import navigate

# Import your modules here...
from app.components import (
    FromTextField, PopularlistComponent,
    ReactivelistComponent
)
from app.controllers import NewsController
from app.models import Article
from app.utils import show_snackbar


class HomePage(FletXPage):
    """Home Page"""

    def __init__(self):
        self.news_ctrl: NewsController = FletX.find(
            NewsController, tag = 'news_ctrl'
        )
        super().__init__(
            padding = padding.only(left=20, right=20, top=0, bottom=0),
            # bgcolor = Colors.BLACK
        )

        # ...

    def on_init(self):
        """Hook called when HomePage in initialized"""

        print("HomePage is initialized")

    def on_destroy(self):
        """Hook called when HomePage will be unmounted."""

        print("HomePage is destroyed")

    def build_categories_tabs(self):
        """Build Categories"""

        tabs = Tabs(
            selected_index = 1,
            animation_duration = 300,

            # TABS
            tabs = [
                Tab(
                    text = category.capitalize(),
                    content = self.build_category_content(category)
                )
                for category in self.news_ctrl.categories
            ]
        )

        return tabs

    def build_category_content(self,category:str):
        """Get category news from controller"""

        news: List[Article] = self.news_ctrl.get_global_context(
            f'{category}_news'
        )

        if not news:
            return Column(
                controls = [
                    Container(
                        height = 100,
                        padding = 10,
                        width = self.width,
                        border_radius = 20,
                        bgcolor = Colors.SURFACE,

                        content = Row(
                            spacing = 10,
                            controls = [
                                # IMAGE CONTAINER
                                Container(
                                    height = 90,
                                    width = 110,
                                    # content = 
                                    data = 'shimmer_load'
                                ),

                                # TITLE AND DESCRIPTION
                                Column(
                                    expand = True,
                                    horizontal_alignment = CrossAxisAlignment.START,
                                    controls = [
                                        # TITLE AND DESCRIPTION SHIMMERS
                                    ]
                                )
                            ]
                        )
                    )
                ]
            )

        return Column(
            spacing = 10,
            controls = [
                Container(
                    ink = True,
                    height = 100,
                    padding = 10,
                    width = self.width,
                    border_radius = 20,
                    bgcolor = Colors.SURFACE,
                    on_click = lambda e: navigate('/details', data = {'article': article}),

                    content = Row(
                        spacing = 10,
                        controls = [
                            # IMAGE CONTAINER
                            Container(
                                height = 90,
                                width = 110,
                                content = Image(
                                    src = article.url_to_image,
                                    fit = ImageFit.COVER,
                                    data = 'shimmer_load'
                                )
                            ),

                            # TITLE AND DESCRIPTION
                            Column(
                                expand = True,
                                horizontal_alignment = CrossAxisAlignment.START,
                                controls = [
                                    Text(
                                        article.title[:30] + '...',
                                        color = Colors.ON_SURFACE,
                                        size = 13,
                                        max_lines = 2,
                                        weight = FontWeight.W_500,
                                        data = 'shimmer_load'
                                    ),
                                    Text(
                                        article.description[:100] + '...',
                                        color = Colors.ON_SURFACE,
                                        size = 11,
                                        max_lines = 3,
                                        weight = FontWeight.W_400,
                                        data = 'shimmer_load'
                                    )
                                ]
                            )
                        ]
                    )
                )
                for article in news
            ]
        )

    def build(self)-> Control:
        """Method that build HomePage content"""

        return SafeArea(
            expand = True,

            # CONTENT
            content = Column(
                expand = True,
                # scroll = ScrollMode.AUTO,
                alignment = MainAxisAlignment.START,
                horizontal_alignment = CrossAxisAlignment.CENTER,
                controls = [
                    # HEADER
                    Container(
                        width = self.width,
                        height = 60,

                        content = Row(
                            expand = True,
                            alignment = MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment = CrossAxisAlignment.CENTER,
                            controls = [
                                Image(
                                    src = "logos/fletx.png",
                                    # width = 50,
                                    height = 60,
                                    # fit = ImageFit.CONTAIN
                                ),
                                IconButton(
                                    icon = Icons.NOTIFICATIONS_NONE_OUTLINED,
                                    icon_size = 30,
                                    icon_color = Colors.ON_SURFACE,
                                    on_click = lambda e: None
                                )
                            ]
                        )
                    ),

                    # SPACER
                    Container(height = 10),

                    # TITLE
                    Text("Explore Today's World News", size = 26, weight=FontWeight.W_600),

                    # SEARCH BAR
                    # Phone number field content
                    Container(
                        height = 50,
                        padding = 10,
                        border_radius = 25,
                        bgcolor = Colors.PRIMARY_CONTAINER,

                        # Content
                        content = FromTextField(
                            # label = "",
                            hint_text = "search...",
                            # rx_value = self.rx_phone,
                            expand = True,
                            filled = False,
                            bgcolor = Colors.TRANSPARENT,
                            focused_bgcolor = Colors.TRANSPARENT,

                            # Border
                            border_radius = 0,
                            border = InputBorder.NONE,

                            # Decoration
                            icon = Icons.SEARCH_OUTLINED
                        ),
                    ),

                    Container(height = 5),  # Spacer

                    Container(
                        expand = True,
                        width = self.width,

                        content = Column(
                            # expand = True,
                            scroll = ScrollMode.AUTO,
                            alignment = MainAxisAlignment.START,
                            horizontal_alignment = CrossAxisAlignment.CENTER,

                            controls = [
                                # POPULAR NEWS
                                Container(
                                    width = self.width,
                                    height = 350,

                                    content = Column(
                                        expand = True,
                                        alignment = MainAxisAlignment.START,
                                        horizontal_alignment = CrossAxisAlignment.CENTER,

                                        controls = [
                                            # Popular News Title
                                            Row(
                                                # expand = True,
                                                alignment = MainAxisAlignment.SPACE_BETWEEN,
                                                vertical_alignment = CrossAxisAlignment.CENTER,
                                                controls = [
                                                    Text("Popular News", size=16, weight=FontWeight.W_600),
                                                    IconButton(
                                                        icon_color=Colors.ON_PRIMARY_CONTAINER,
                                                        on_click = lambda e: show_snackbar(
                                                            self.page,
                                                            type = 'warning',
                                                            title = 'Alert!',
                                                            message = 'No content available here... there\'s no page here....'
                                                        ),

                                                        content = Row(
                                                            controls = [
                                                                Text("See all", size=14, weight=FontWeight.W_500),
                                                                Icon(Icons.ARROW_FORWARD, size=16, color=Colors.ON_PRIMARY_CONTAINER)
                                                            ]
                                                        )
                                                    )
                                                ]
                                            ),

                                            # Popular News List
                                            Container(
                                                expand = True,
                                                width = self.width,
                                                # bgcolor="red",

                                                content = PopularlistComponent(
                                                    rx_items = self.news_ctrl.popular_news,
                                                )
                                            )
                                        ]
                                    )
                                ),

                                # SPACER
                                Container(height = 20),
                                
                                # CATEGORIES LIST
                                Column(
                                    expand = True,
                                    alignment = MainAxisAlignment.START,
                                    horizontal_alignment = CrossAxisAlignment.CENTER,

                                    controls = [
                                        # Popular News Title
                                        Row(
                                            # expand = True,
                                            alignment = MainAxisAlignment.SPACE_BETWEEN,
                                            vertical_alignment = CrossAxisAlignment.CENTER,
                                            controls = [
                                                Text("Top Categories", size=16, weight=FontWeight.W_600),
                                                IconButton(
                                                    icon_color=Colors.ON_PRIMARY_CONTAINER,
                                                    on_click = lambda e: show_snackbar(
                                                        self.page,
                                                        type = 'warning',
                                                        title = 'Alert!',
                                                        message = 'No content available here... there\'s no page here....'
                                                    ),

                                                    content = Row(
                                                        controls = [
                                                            Text("See all", size=14, weight=FontWeight.W_500),
                                                            Icon(Icons.ARROW_FORWARD, size=16, color=Colors.ON_PRIMARY_CONTAINER)
                                                        ]
                                                    )
                                                )
                                            ]
                                        ),
                                        self.build_categories_tabs(),
                                    ]
                                )
                            ]
                        )
                    ),

                ]
            )
        )