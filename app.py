import re
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi


# --------------------------------------------------
# Environment Setup
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env", override=True)

ANSI_ESCAPE_RE = re.compile(r"\x1B\[[0-?]*[ -/]*[@-~]")


# --------------------------------------------------
# Utility Functions
# --------------------------------------------------

def sanitize_error_message(message: str) -> str:
    return ANSI_ESCAPE_RE.sub("", message or "").strip()


def is_supported_link(url: str) -> bool:
    pattern = re.compile(
        r"^(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+$",
        re.IGNORECASE,
    )
    return bool(pattern.match(url.strip()))


def extract_video_id(url: str) -> str | None:
    parsed_url = urlparse(url)

    if parsed_url.hostname in ["www.youtube.com", "youtube.com"]:
        return parse_qs(parsed_url.query).get("v", [None])[0]

    if parsed_url.hostname == "youtu.be":
        return parsed_url.path[1:]

    return None


# --------------------------------------------------
# Expected Output
# --------------------------------------------------

"""
{
    "video_id": "abc123xyz",
    "youtube_url": "https://www.youtube.com/watch?v=abc123xyz",
    "language": "en",
    "transcription": "Full transcript text extracted from YouTube video..."
}
"""


# --------------------------------------------------
# Error Handling
# --------------------------------------------------

"""
Handled Errors:
- Invalid YouTube URL
- Unsupported URL format
- Missing transcript/captions
- Disabled captions
- Private video
- Video unavailable
- Unsupported language
"""


# --------------------------------------------------
# Transcript Extraction
# --------------------------------------------------

def get_transcript(video_id: str, language: str = "en") -> str:
    try:
        transcript = YouTubeTranscriptApi().fetch(
            video_id,
            languages=[language]
        )

        return " ".join(
            [item.text for item in transcript]
        )

    except Exception as err:
        error_message = sanitize_error_message(str(err)).lower()

        if "transcriptsdisabled" in error_message:
            raise RuntimeError(
                "Transcripts are disabled for this video."
            ) from err

        if "novideotranscriptfound" in error_message:
            raise RuntimeError(
                f"No transcript found for language: {language}"
            ) from err

        if "private video" in error_message:
            raise RuntimeError(
                "This YouTube video is private."
            ) from err

        if "video unavailable" in error_message:
            raise RuntimeError(
                "The YouTube video is unavailable or private."
            ) from err

        raise RuntimeError(
            sanitize_error_message(str(err))
        ) from err

# --------------------------------------------------
# Main Execution
# --------------------------------------------------

if __name__ == "__main__":

    youtube_url = input("Enter YouTube URL: ").strip()
    language = input("Enter language (default=en): ").strip() or "en"

    if not youtube_url:
        raise ValueError("YouTube URL is required.")

    if not is_supported_link(youtube_url):
        raise ValueError("Unsupported YouTube URL.")

    video_id = extract_video_id(youtube_url)

    if not video_id:
        raise ValueError("Could not extract YouTube video ID.")

    transcript = get_transcript(video_id, language)

    result = {
        "video_id": video_id,
        "youtube_url": youtube_url,
        "language": language,
        "transcription": transcript,
    }

    print("\nTranscript Extraction Successful\n")
    print(result)