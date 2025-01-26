import os
from pathlib import Path
from dotenv import load_dotenv
import yaml

def load_config():
    # Load environment variables
    load_dotenv(override=True)
    
    # Load default config
    config_path = Path(__file__).parent / "default_settings.yaml"
    with open(config_path) as f:
        config = yaml.safe_load(f)
    
    # Environment variables take precedence
    for key in config:
        env_val = os.getenv(key.upper())
        if env_val:
            config[key] = env_val
            
    return config