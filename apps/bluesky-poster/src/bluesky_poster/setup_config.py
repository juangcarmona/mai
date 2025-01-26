from questionary import confirm, text

def setup_wizard():
    print("🚀 Bluesky Poster Configuration Wizard")
    
    config = {
        "BLUESKY_HANDLE": text("Enter your Bluesky handle:").ask(),
        "BLUESKY_APP_PASSWORD": text("Enter your Bluesky app password:", password=True).ask(),
        "NEWS_API_KEY": text("Enter NewsAPI key (optional):").ask(),
        "OPENAI_API_KEY": text("Enter OpenAI API key (optional):").ask(),
        "DEEPSEEK_API_KEY": text("Enter DeepSeek API key (optional):").ask()
    }
    
    if confirm("Save these to .env file?").ask():
        with open(".env", "w") as f:
            for key, value in config.items():
                if value:  # Only write non-empty values
                    f.write(f"{key}={value}\n")
        print("Configuration saved to .env file")
        
    return config