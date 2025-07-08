from flet import *
from fletx.core import FletXController
from .theme import dark_gradient
from .images import with_random_img

__all__ = [
    'dark_gradient',
    'with_random_img',
    'show_loader',
    'show_snackbar'
]

def show_loader(controller: FletXController,page: Page):
        """Show loading when controller is in loading state."""

        if hasattr(show_loader,'dlg'):
            dlg = getattr(show_loader,'dlg')

        else: 
            dlg = AlertDialog(
                content_padding = 10,
                title = Text(
                    "Fetching News....",
                    size = 14,
                    text_align = TextAlign.CENTER
                ),
                content = Row(
                    expand = True,
                    alignment = MainAxisAlignment.CENTER,
                    vertical_alignment = CrossAxisAlignment.CENTER,
                    controls = [
                        ProgressRing(
                            width=40, height=40
                        ),
                    ]
                ),
                alignment = alignment.center,
                on_dismiss = lambda e: print("Dialog dismissed!"),
                title_padding = padding.all(25),
            )


        if controller._is_loading.value:
            page.open(dlg)

        else: 
            page.close(dlg)

        show_loader.dlg = dlg

def show_snackbar(
    page: Page,
    title: str, 
    message: str, 
    type: str = 'info'
):
    """Show a snackbar"""

    bg = Colors.PRIMARY

    def get_icon():
        nonlocal type
        nonlocal bg

        if type == 'info':
            return Icons.INFO_OUTLINE_ROUNDED
        
        if type == 'error':
            bg = Colors.ERROR_CONTAINER
            return Icons.ERROR_OUTLINE_ROUNDED
        
        if type == 'warning':
            bg = Colors.AMBER_800
            return Icons.WARNING_AMBER_OUTLINED
        
        if type == 'success':
            bg = Colors.TEAL_400
            return Icons.EMOJI_EMOTIONS_OUTLINED
        
        return Icons.FAVORITE_BORDER_OUTLINED
    
    right_icon = get_icon()

    snack = SnackBar(
        bgcolor = bg,
        content = Container(
            expand = True,
            padding = 10,
            bgcolor = bg,
            content = Row(
                expand = True,
                alignment = MainAxisAlignment.START,
                vertical_alignment = CrossAxisAlignment.CENTER,
                controls = [
                    # RIGHT ICON
                    Icon(
                        right_icon,
                        size = 40,
                    ),
                    
                    # TEXTS
                    Column(
                        expand = True,
                        alignment = MainAxisAlignment.CENTER,
                        horizontal_alignment = CrossAxisAlignment.START,

                        controls = [
                            Text(
                                title[:50] ,
                                color = Colors.ON_SURFACE,
                                size = 18,
                                max_lines = 2,
                                weight = FontWeight.W_600
                            ),
                            Text(
                                message[:150],
                                color = Colors.ON_SURFACE,
                                size = 14,
                                max_lines = 3,
                                weight = FontWeight.W_400
                            )
                        ]
                    )
                ]
            )
        )
    )

    page.open(snack)