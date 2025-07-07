"""
Taskio App
None

A FletX application.
Author: pro2015
Version: 0.1.0
"""

import flet as ft
from dotenv import load_dotenv
from fletx.app import FletXApp
from app.routes import TaskioRouter
from app.utils.theme import light_theme, dark_theme

# Load environment variables
load_dotenv()

def main():
    """Main entry point for the Taskio application."""

    # Lifecycle Hooks 
    async def on_startup(page: ft.Page):
        print("App is running!")
        page.padding = 0
    
    def on_shutdown(page: ft.Page):
        print("App is closed!")
    
    # App Configuration
    app = FletXApp(
        title="Taskio",
        initial_route = "/welcome",
        debug = True,
        theme = light_theme,
        dark_theme = dark_theme,
        window_config = {
            "width": 400,
            "height": 810,
            "resizable": True,
            "maximizable": True
        },
        on_startup = on_startup,
        on_shutdown = on_shutdown
    )

    # Run App
    app.run_async()     # you can use also `app.run()` method. see documetation for more

if __name__ == "__main__":
    main()