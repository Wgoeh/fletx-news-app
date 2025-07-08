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
    HomePage, DetailsPage
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
    },
    {
        'path': '/',
        'component': HomePage,
    },
    {
        'path': '/details',
        'component': DetailsPage,
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