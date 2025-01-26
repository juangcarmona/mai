import requests
import os
from bluesky_poster.logger import get_logger

logger = get_logger("local_inference")

class LocalInferenceClient:
    def __init__(self):
        self.base_url = os.getenv("LOCAL_INFERENCE_URL", "http://localhost:8080")
        self.auth_token = os.getenv("LOCAL_INFERENCE_TOKEN")
        logger.debug(f"Using local inference endpoint: {self.base_url}")

    def generate_post(self, prompt: str) -> str:
        """
        Generate a Bluesky post using a local inference endpoint.
        
        Args:
            prompt (str): The full prompt to send to the inference API, including topic, hashtags, and news context.
        
        Returns:
            str: The generated post content.
        """
        try:
            headers = {}
            if self.auth_token:
                headers["Authorization"] = f"Bearer {self.auth_token}"
            
            # Updated payload for LLM Studio
            payload = {
                "model": "mathstral-7b-v0.1",  # Replace with your model name
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant that generates engaging Bluesky posts."},
                    {"role": "user", "content": prompt}
                ],
                "max_tokens": 100,
                "temperature": 0.7,
            }
            
            response = requests.post(
                f"{self.base_url}/v1/chat/completions",
                json=payload,
                headers=headers,
            )
            response.raise_for_status()
            
            # Extract the response content
            response_data = response.json()
            if not response_data.get("choices") or not response_data["choices"][0].get("message", {}).get("content"):
                logger.error("No content found in the API response.")
                raise ValueError("No content found in the API response.")
            
            return response_data["choices"][0]["message"]["content"].strip()
        except Exception as e:
            logger.error(f"Failed to generate post with local inference: {str(e)}")
            raise