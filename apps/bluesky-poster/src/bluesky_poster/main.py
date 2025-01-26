from questionary import select, text, confirm
from bluesky_poster.auth.authenticate import authenticate
from bluesky_poster.local_inference_client import LocalInferenceClient
from bluesky_poster.news_client import NewsClient
from bluesky_poster.post.poster import create_simple_post
from bluesky_poster.logger import configure_logger, get_logger
from bluesky_poster.post.poster import generate_link_embed
import os

# Configure root logger
configure_logger()
logger = get_logger()

def calculate_available_chars(hashtags: str, personal_motto: str) -> int:
    """
    Calculate the available characters for the LLM-generated text.
    New post structure: "{llm_generated_text}\n\n{personal_motto}\n{hashtags}"
    """
    fixed_parts_length = (
        len(personal_motto) +
        len(hashtags) + 4  # 4 characters for newlines between sections
    )
    return 300 - fixed_parts_length


def truncate_text(text: str, max_length: int) -> str:
    """Truncate text to ensure it doesn't exceed the max length."""
    if len(text) <= max_length:
        return text
    return text[:max_length - 4] + "..."  # Add ellipsis if truncated

def get_user_choice(field_name: str, default_value: str) -> str:
    """
    Prompt the user to choose between using the default value, providing a custom value,
    or skipping the field entirely.
    """
    choice = select(
        f"What would you like to do for {field_name}?",
        choices=[
            {"name": f"Use default: {default_value}", "value": "default"},
            {"name": "Enter a custom value", "value": "custom"},
            {"name": "Don't use this field", "value": "skip"},
        ],
    ).ask()

    if choice == "default":
        return default_value
    elif choice == "custom":
        return text(f"Enter your custom {field_name}:").ask()
    elif choice == "skip":
        return ""
    else:
        raise ValueError("Invalid choice")

def main():
    try:
        logger.info("Starting Bluesky Poster application")
        client = authenticate()
        local_client = LocalInferenceClient()
        news_client = NewsClient()

        # Get user input for the topic
        topic = text("What should the post be about?").ask()
        if not topic:
            logger.error("No topic provided. Exiting.")
            return

        # Get user input for hashtags
        default_hashtags = os.getenv("PREFERRED_HASHTAGS", "#AIRevolution #FutureOfWork")
        hashtags = get_user_choice("hashtags", default_hashtags)

        # Get user input for personal motto
        default_motto = os.getenv("PERSONAL_MOTTO", "Your AI, your rules. Shape your future on your terms.")
        personal_motto = get_user_choice("personal motto", default_motto)

        # Fetch news articles related to the topic
        logger.info(f"Fetching news articles about: {topic}...")
        news_articles = news_client.fetch_news_by_topic(topic)

        # Iterate through news articles
        for article in news_articles:
            title = article.get("title", "No title")
            description = article.get("description", "No description")
            url = article.get("url", "#")

            # Show the article summary to the user
            logger.info(f"\n\nFound article:\n{title}\n{description}\nURL: {url}\n\n\n")
            post_about_this = confirm("Do you want to post about this article?").ask()
            if not post_about_this:
                continue

            # Calculate available characters for the LLM-generated text
            available_chars = calculate_available_chars(hashtags, personal_motto)
            logger.debug(f"Available characters for LLM-generated text: {available_chars}")

            # Generate a prompt for the LLM
            prompt = (
                f"Generate a short, engaging Bluesky post about this article: {title}. "
                f"Summary: {description}. "
                f"Keep the tone professional but approachable. "
                f"Limit the post to {available_chars} characters."
            )

            # Generate a post using the local client
            logger.info("Generating post with local inference...")
            draft = local_client.generate_post(prompt)
            logger.info(f"Generated draft post: {draft}")

            # Truncate the LLM-generated text if necessary
            truncated_draft = truncate_text(draft, available_chars)

            # Construct the final post
            final_post_parts = [truncated_draft]
            if personal_motto:
                final_post_parts.append(personal_motto)
            if hashtags:
                final_post_parts.append(hashtags)
            final_post = "\n\n".join(final_post_parts)

            # Validate the total grapheme count
            if len(final_post) > 300:
                logger.error(f"Post exceeds 300 graphemes: {len(final_post)}")
                continue

            # Show the final post to the user and ask for confirmation
            publish_post = confirm(f"Post this?\n\n{final_post}").ask()
            if publish_post:
                embed = generate_link_embed(
                        url=url,
                        title=title,
                        description=description
                    )
                create_simple_post(client, final_post, embed)
                logger.info("Post published successfully!")
                break  # Exit after publishing one post

    except Exception as e:
        logger.exception("Application failed with error: %s", str(e))
        raise

if __name__ == "__main__":
    main()

