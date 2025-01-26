from openai import OpenAI
import os
from bluesky_poster.logger import get_logger

logger = get_logger("chatgpt")

class OpenAIClient:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def generate_post(self, topic: str, hashtags: str) -> str:
        """Generate a Bluesky post using ChatGPT's API."""
        try:
            prompt = (
                f"Generate a short, engaging Bluesky post about: {topic}. "
                f"Include these hashtags: {hashtags}. "
                "Keep the tone professional but approachable. "
                "Limit the post to 300 characters."
            )
            response = self.client.chat.completions.create(
                model="gpt-4",  # Use gpt-3.5-turbo if you don't have GPT-4 access
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that generates engaging Bluesky posts."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=100
            )
            # Validate the response
            if not response.choices or not response.choices[0].message.content:
                logger.error("No content found in the API response.")
                raise ValueError("No content found in the API response.")

            return response.choices[0].message.content.strip()
        except Exception as e:
            logger.error(f"Failed to generate post with ChatGPT: {str(e)}")
            raise