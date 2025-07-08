"""
Taskio Application Pages module.

This module contains the application Pages.
Version: 0.1.0
"""

from .counter import CounterPage
from .onboarding_page import OnboardingPage
from .home_page import HomePage
from .details_page import DetailsPage

__all__ = [
    'CounterPage',
    'OnboardingPage',
    'HomePage',
    'DetailsPage'
]