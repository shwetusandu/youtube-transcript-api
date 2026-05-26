# YouTube Transcript API

AI-powered Apify Actor to extract YouTube video transcripts quickly and return structured text output for automation workflows, AI pipelines, and content processing systems.

---

# 🚀 Overview

This project extracts transcripts from public YouTube videos using `youtube-transcript-api`.

The actor:
- Accepts a YouTube video URL
- Extracts available captions/transcripts
- Returns structured JSON output
- Supports multiple languages
- Handles common YouTube transcript errors

Built with:
- Python
- Apify
- youtube-transcript-api
- Docker

---

# 🎯 Problem Solved

Manually copying YouTube transcripts is:
- Time-consuming
- Inconsistent
- Difficult to automate
- Not scalable

This actor automates transcript extraction for:
- AI workflows
- Content repurposing
- Knowledge systems
- SEO pipelines
- Research workflows

---

# 💼 Real-World Use Cases

## 1. AI Content Repurposing
Convert YouTube videos into:
- Blog posts
- LinkedIn posts
- Twitter threads
- Email summaries

## 2. Knowledge Extraction
Feed transcripts into:
- Vector databases
- RAG systems
- AI agents
- Search systems

## 3. Research Automation
Extract transcripts for:
- Learning
- Analysis
- Summaries
- Documentation

## 4. Subtitle Processing
Use transcript output for:
- Caption workflows
- Translation pipelines
- Accessibility systems

---

# 🏗️ Project Structure

```bash
.
├── app.py
├── main.py
├── apify.json
├── input_schema.json
├── requirements.txt
├── Dockerfile
├── .env.example
├── README.md
└── .gitignore
```

---

# ⚙️ Features

- YouTube transcript extraction
- Multi-language support
- Structured JSON output
- Fast lightweight architecture
- Docker support
- Apify-ready deployment
- Error handling support

---

# 🔧 Input

Example input:

```json
{
  "youtube_url": "https://www.youtube.com/watch?v=example",
  "language": "en"
}
```

---

# 📤 Expected Output

```json
{
  "video_id": "abc123xyz",
  "youtube_url": "https://www.youtube.com/watch?v=abc123xyz",
  "language": "en",
  "transcription": "Full transcript text extracted from YouTube video..."
}
```

---

# ⚠️ Error Handling

Handled scenarios:
- Invalid YouTube URL
- Unsupported URL format
- Missing transcript/captions
- Disabled captions
- Private video
- Video unavailable
- Unsupported language

---

# 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Runtime | Python |
| Platform | Apify |
| Transcript Engine | youtube-transcript-api |
| Containerization | Docker |
| Environment Management | python-dotenv |

---

# ▶️ How to Run Locally

## 1. Clone Repository

```bash
git clone <your-repository-url>
cd YOUTUBE-TRANSCRIPT-API
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run Project

```bash
python app.py
```

---

# 🐳 Docker Support

Build Docker image:

```bash
docker build -t youtube-transcript-api .
```

Run container:

```bash
docker run youtube-transcript-api
```

---

# ☁️ Deploy to Apify

## Login

```bash
apify login
```

## Push Actor

```bash
apify push
```

---

# 📊 Workflow Overview

```text
Input YouTube URL
        ↓
Validate URL
        ↓
Extract Video ID
        ↓
Fetch Transcript
        ↓
Structure Output
        ↓
Return JSON Response
```

---

# ✅ Best Practices Implemented

- Input validation
- Structured JSON outputs
- Minimal architecture
- Lightweight dependency stack
- Error handling
- Clean folder structure
- Dockerized deployment

---

# 🔒 Security Notes

- No API keys required
- No cookies required
- No browser automation
- No credential storage

---

# 🧪 Recommended Testing

Before deployment:
- Test valid YouTube videos
- Test invalid URLs
- Test videos without captions
- Test private videos
- Validate Docker build
- Validate Apify deployment

---

# 📸 Screenshots

Recommended screenshots:
- Apify Actor page
- Input form
- Successful transcript output
- Logs
- Dataset output

---

# 📈 Future Improvements

Potential enhancements:
- Batch URL processing
- Transcript summarization
- OpenAI integration
- Subtitle export
- Keyword extraction
- Speaker segmentation
- Translation workflows

---

# 🤝 Contributing

Contributions are welcome.

Suggested improvements:
- Better transcript formatting
- Additional language support
- Improved validation
- Performance optimization

---

# 📄 License

MIT License

---

# ⭐ Support

If this project helps you:
- Star the repository
- Fork the project
- Share feedback
- Suggest improvements

---

# 📌 Notes

This project follows automation best practices:
- Keep workflows simple
- Validate inputs early
- Use structured outputs
- Avoid unnecessary complexity
