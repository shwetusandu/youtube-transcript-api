# YouTube Transcript Extractor

Extract transcripts from YouTube videos using youtube-transcript-api with structured JSON output and multi-language support.

## Features

- Extract YouTube transcripts
- Multi-language support
- JSON output
- Apify-ready workflow

## Input

```json
{
  "youtube_url": "https://www.youtube.com/watch?v=H8Lyj2D_cWo",
  "language": "hi"
}

## Output

{
  "video_id": "H8Lyj2D_cWo",
  "language": "hi",
  "transcription": "Transcript text..."
}