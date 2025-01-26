import os
import requests
from typing import List, Dict
from bluesky_poster.logger import get_logger

logger = get_logger("news_client")

class NewsClient:
    def __init__(self):
        self.api_key = os.getenv("NEWS_API_KEY")  # Add your news API key to the environment
        self.base_url = "https://newsapi.org/v2/everything"  # Example using NewsAPI

    def fetch_news_by_topic(self, topic: str) -> List[Dict]:
        """Fetch news articles based on a user-provided topic."""
        news_results = []
        try:
            params = {
                "q": topic,
                "apiKey": self.api_key,
                "pageSize": 5,  # Limit to 5 articles
                "sortBy": "publishedAt",  # Get the latest news
            }
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            articles = response.json().get("articles", [])
            news_results.extend(articles)
            logger.info(f"Fetched {len(news_results)} news articles about: {topic}.")
            return news_results
        except Exception as e:
            logger.error(f"Failed to fetch news: {str(e)}")
            raise