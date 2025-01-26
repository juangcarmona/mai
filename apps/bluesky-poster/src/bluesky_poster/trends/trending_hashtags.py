import re
from collections import Counter
from typing import List, Tuple
from atproto import Client
from bluesky_poster.logger import get_logger

logger = get_logger("trends")

def get_trending_hashtags(client: Client, limit: int = 100) -> List[Tuple[str, int]]:
    """Fetch recent posts and extract trending hashtags using atproto client"""
    logger.debug("Starting hashtag search with limit %d", limit)
    
    try:
        # search_result = client.bsky.feed.search_posts(q="", limit=limit)
        # logger.info("Found %d posts for analysis", len(search_result.posts))
        
        hashtags = []
        # for post in search_result.posts:
        #     if post.record.text:
        #         text = post.record.text.lower()
        #         hashtags.extend(re.findall(r'#(\w+)', text))
        
        counter = Counter(hashtags)
        logger.debug("Hashtag frequency: %s", counter.most_common(10))
        
        return counter.most_common(5)
    except Exception as e:
        logger.error("Failed to fetch trending hashtags: %s", str(e))
        raise