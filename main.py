from pathlib import Path
import os
import uuid

from apify import Actor

from app import (
    analyze_description_only,
    analyze_transcript,
    download_audio,
    extract_video_description,
    is_supported_link,
    save_groq_summary_to_md,
    save_transcript_to_file,
    transcribe_audio,
)


async def main() -> None:
    async with Actor:
        actor_input = await Actor.get_input() or {}
        source_url = str(actor_input.get("source_url", "")).strip()
        cookies_txt = str(actor_input.get("instagram_cookies_txt", "")).strip()

        if not source_url:
            raise ValueError("Missing required input: source_url")
        if not is_supported_link(source_url):
            raise ValueError("Only YouTube or Instagram links are supported.")

        if cookies_txt:
            cookie_path = Path("/tmp/instagram-cookies.txt")
            cookie_path.write_text(cookies_txt, encoding="utf-8")
            os.environ["YTDLP_COOKIES_FILE"] = str(cookie_path)

        job_id = str(uuid.uuid4())

        video_description = extract_video_description(source_url)
        audio_path = download_audio(source_url, job_id)
        transcript = transcribe_audio(audio_path, job_id)

        transcript_file = ""
        if not transcript:
            status_message = "Transcription is empty. Extracted only description"
            qa_summary = analyze_description_only(video_description)
        else:
            status_message = "Completed"
            transcript_file = str(save_transcript_to_file(transcript))
            qa_summary = analyze_transcript(transcript, video_description)

        summary_file = str(
            save_groq_summary_to_md(
                qa_summary=qa_summary,
                description=video_description,
                transcript=transcript,
            )
        )

        result = {
            "source_url": source_url,
            "status": status_message,
            "video_description": video_description,
            "transcript": transcript,
            "qa_summary": qa_summary,
            "transcript_file": transcript_file,
            "summary_file": summary_file,
        }

        await Actor.push_data(result)
        await Actor.set_value("OUTPUT", result)


if __name__ == "__main__":
    Actor.run(main)
