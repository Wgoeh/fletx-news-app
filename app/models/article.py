from dataclasses import dataclass
from typing import Optional


####
##      ARTICLE SOURCE MODEL
#####
@dataclass
class ArticleSource:
    """Represent an Article source."""
    
    id: str
    name: str


####
##      ARTICLE MODEL
#####
@dataclass
class Article:
    """Represent an Article."""

    author: str
    title: str
    description: str
    url: str
    url_to_image: str
    published_at: str
    content: str
    source: Optional[ArticleSource] = None

