import os
import re
from crewai_tools import YoutubeVideoSearchTool

# Set the OpenAI model name
os.environ["OPENAI_MODEL_NAME"] = "gpt-3.5-turbo"


def is_valid_youtube_url(url: str) -> bool:
    """
    Validate if the provided URL is a valid YouTube video URL.
    It must contain a valid 11-character video ID.
    """
    youtube_regex = re.compile(
        r'^(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/)([\w\-]{11})'
    )
    return bool(youtube_regex.match(url.strip()))


def get_yt_tool(video_url: str, user_api_key: str):
    """
    Validates YouTube URL and sets up the YoutubeVideoSearchTool.
    Prevents fallback to invalid 'abcd1234' video ID.
    """
    if not is_valid_youtube_url(video_url):
        raise ValueError(f"Invalid YouTube video URL provided: {video_url}")

    # Set OpenAI API key in environment
    os.environ["OPENAI_API_KEY"] = user_api_key

    # Return the search tool
    return YoutubeVideoSearchTool(video_url=video_url)
