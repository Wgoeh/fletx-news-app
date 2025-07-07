"""
taskio Application routing module.
Version: 0.1.0
"""


# Import your pages here
from fletx.navigation import (
    ModuleRouter, TransitionType, RouteTransition
)
from fletx.decorators import register_router

from .pages import (
    CounterPage, OnboardingPage,
    HomePage
)

# Define Taskio routes here
routes = [
    {
        'path': '/counter',
        'component': CounterPage,
    },
    {
        'path': '/welcome',
        'component': OnboardingPage,
        # 'meta': {
        #     'transition': RouteTransition(
        #         type=TransitionType.NONE,
        #         duration=500,
        #     )
        # }
    },
    {
        'path': '/',
        'component': HomePage,
        'meta': {
            'transition': RouteTransition(
                type = TransitionType.FADE,
                duration = 350,
            )
        }
    }
]

@register_router
class TaskioRouter(ModuleRouter):
    """taskio Routing Module."""

    name = 'taskio'
    base_path = '/'
    is_root = True
    routes = routes
    sub_routers = []