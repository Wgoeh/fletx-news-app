"""
Details Controller.

This Page class is generated from a template.
"""

from flet import *
from fletx.core import FletXPage
from fletx.navigation import go_back

# Import your modules here...
from app.models import Article
from app.utils import dark_gradient


class DetailsPage(FletXPage):
    """Details Page"""

    def __init__(self):
        self.article: Article
        super().__init__(
            padding = 0,
            bgcolor = Colors.SURFACE
        )

        # ...
        # self.article: Article = self.route_info.data.get('article')

    def on_init(self):
        """Hook called when DetailsPage in initialized"""

        print("DetailsPage is initialized")

    def on_destroy(self):
        """Hook called when DetailsPage will be unmounted."""

        print("DetailsPage is destroyed")

    def build(self)-> Control:
        """Method that build DetailsPage content"""

        self.article = self.route_info.data.get('article')

        return SafeArea(
            expand = True,
            content = Container(
                expand = True,
                # height = self.height,
                width = self.width,

                content = Stack(
                    expand = True,
                    alignment = alignment.top_center,
                    controls = [
                        # IMAGE CONTAINER
                        Container(
                            # height = self.width,
                            expand = True,
                            width = self.width,

                            content = Stack(
                                expand = True,
                                alignment = alignment.top_center,
                                controls = [
                                    Image(
                                        src = self.article.url_to_image,
                                        width = self.width,
                                        fit = ImageFit.FIT_WIDTH
                                    ),

                                    Column(
                                        expand = True,
                                        spacing = 0,
                                        controls = [
                                            Container(
                                                expand = True,
                                                # height = self.width,
                                                width = self.width,

                                                gradient = dark_gradient
                                            ),

                                            Container(
                                                expand = True,
                                                width = self.width,
                                                # bgcolor = "red"
                                            ),
                                            Container(
                                                height = 170,
                                                width = self.width,
                                                bgcolor = "red"
                                            )
                                        ]
                                    )
                                ]
                            )
                        ),

                        # INFO CONTAINER
                        Container(
                            expand = True,
                            width = self.width,
                            content = Column(
                                spacing = 0,
                                expand = True,
                                alignment = MainAxisAlignment.START,
                                horizontal_alignment = CrossAxisAlignment.START,
                                controls = [
                                    Container(
                                        height = 70,
                                        width = self.width,
                                        content = Row(
                                            expand = True,
                                            alignment = MainAxisAlignment.SPACE_BETWEEN,
                                            vertical_alignment = CrossAxisAlignment.CENTER,
                                            controls = [
                                                IconButton(
                                                    icon = Icons.CHEVRON_LEFT_OUTLINED,
                                                    icon_size = 38,
                                                    icon_color = Colors.ON_PRIMARY,
                                                    on_click = lambda e: go_back()
                                                )
                                            ]
                                        )
                                    ),

                                    # SPACER
                                    Container(
                                        height = 70,
                                    ),

                                    Container(
                                        # expand = True,
                                        width = self.width,
                                        # bgcolor = Colors.PRIMARY,
                                        padding = Padding(left= 20, right = 20, top = 0, bottom = 0),

                                        content = Column(
                                            expand = True,
                                            controls = [
                                                # ARTICLE SOURCE
                                                Container(
                                                    padding = 6,
                                                    bgcolor = Colors.PRIMARY_CONTAINER,
                                                    border_radius = 5,
                                                    content = Text(
                                                        self.article.source.name,
                                                        size = 14,
                                                        weight = FontWeight.W_600,
                                                        color = Colors.ON_PRIMARY
                                                    ),
                                                    # alignment = alignment.center_right
                                                ),

                                                # TITLE
                                                Text(
                                                    self.article.title,# "Here's what you need to know about FletX!", 
                                                    size = 20,
                                                    max_lines = 3,
                                                    weight = FontWeight.W_600
                                                ),

                                            ]
                                        )
                                    ),

                                    # DETAILS
                                    Container(
                                        expand = True,
                                        width = self.width,
                                        border_radius = BorderRadius(
                                            top_left = 20,
                                            top_right = 20,
                                            bottom_left = 0,
                                            bottom_right = 0
                                        ),
                                        bgcolor = Colors.SURFACE,
                                        padding = Padding(left= 20, right = 20, top = 20, bottom = 0),

                                        content = Column(
                                            expand= True,
                                            scroll = ScrollMode.AUTO,

                                            controls = [
                                                Markdown(
                                                    self.article.content,
                                                    expand = True,
                                                    shrink_wrap = True,
                                                    selectable = True,
                                                    extension_set = MarkdownExtensionSet.GITHUB_WEB,
                                                    code_theme = MarkdownCodeTheme.DARCULA,
                                                    auto_follow_links = True
                                                )
                                            ]
                                        )
                                    )
                                ]
                            )
                        )
                    ]
                )
            )
        )