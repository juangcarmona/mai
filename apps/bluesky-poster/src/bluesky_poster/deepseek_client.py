from openai import OpenAI
import os
from bluesky_poster.logger import get_logger

logger = get_logger("deepseek")

class DeepSeekClient:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("DEEPSEEK_API_KEY"),
            base_url="https://api.deepseek.com"
        )

    def generate_post(self, topic: str, hashtags: str) -> str:
        """Generate a Bluesky post using DeepSeek's API."""
        try:
            prompt = (
                f"Generate a short, engaging Bluesky post about: {topic}. "
                f"Include these hashtags: {hashtags}. "
                "Keep the tone professional but approachable. "
                "Limit the post to 300 characters."
            )
            response = self.client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that generates engaging Bluesky posts."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=100
            )            # Validate the response
            if not response.choices or not response.choices[0].message.content:
                logger.error("No content found in the API response.")
                raise ValueError("No content found in the API response.")

            return response.choices[0].message.content.strip()
        except Exception as e:
            logger.error(f"Failed to generate post with DeepSeek: {str(e)}")
            raise