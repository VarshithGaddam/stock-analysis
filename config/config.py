# config/config.py
config_list = [
    {
        "model": "gemini-1.5-flash",  # Using Gemini 1.5 Flash for efficiency
        "api_key": "your-api-key",  # Your Gemini API key
        "base_url": "https://generativelanguage.googleapis.com/v1beta/"  # Gemini OpenAI-compatible endpoint
    }
]

# API timeout settings
REQUEST_TIMEOUT = 120 