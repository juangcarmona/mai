from atproto import Client, models
from atproto import models
from atproto_client.utils import TextBuilder
from bluesky_poster.logger import get_logger
from typing import Optional, List, Union

logger = get_logger("post")

def create_post(
    client: Client,
    text: Union[str, TextBuilder],
    profile_identify: Optional[str] = None,
    reply_to: Optional[models.AppBskyFeedPost.ReplyRef] = None,
    embed: Optional[
        Union[
            models.AppBskyEmbedImages.Main,
            models.AppBskyEmbedExternal.Main,
            models.AppBskyEmbedRecord.Main,
            models.AppBskyEmbedRecordWithMedia.Main,
            models.AppBskyEmbedVideo.Main,
        ]
    ] = None,
    langs: Optional[List[str]] = None,
    facets: Optional[List[models.AppBskyRichtextFacet.Main]] = None
) -> models.AppBskyFeedPost.CreateRecordResponse:
    """Create a Bluesky post with proper formatting and extended features"""
    logger.debug("Attempting to create post with text: %s", text)
    
    try:
        # If no languages specified, default to English
        if not langs:
            langs = ['en']
            logger.debug("Using default language: %s", langs)
        
        # Create the post
        result = client.send_post(
            text=text,
            profile_identify=profile_identify,
            reply_to=reply_to,
            embed=embed,
            langs=langs,
            facets=facets
        )
        
        logger.info("Post created successfully: %s", result.uri)
        return result
    except Exception as e:
        logger.error("Failed to create post: %s", str(e))
        raise

def create_simple_post(
    client: Client, 
    text: str,
    embed: Optional[models.AppBskyEmbedExternal.Main] = None
) -> models.AppBskyFeedPost.CreateRecordResponse:
    """Simplified post creation for basic text posts with optional embed."""
    logger.debug("Creating simple post with text: %s", text)
    return create_post(client, text, embed=embed)



def generate_link_embed(url: str, title: str, description: str) -> models.AppBskyEmbedExternal.Main:
    """Create a link card embed using article metadata."""
    return models.AppBskyEmbedExternal.Main(
        external=models.AppBskyEmbedExternal.External(
            uri=url,
            title=title[:300],  # Truncate if necessary
            description=description[:1000]  # Truncate long descriptions
        )
    )