from moviepy import VideoFileClip
from pathlib import Path
from .utils import get_output_path

def video_to_mp3(file_path):
    if not Path(file_path).is_file():
        print("❌ File not found.")
        return

    try:
        print(f"🎞️ Converting: {file_path}")
        video = VideoFileClip(file_path)
        audio = video.audio

        output_name = f"{Path(file_path).stem}.mp3"
        output_path = get_output_path(file_path, output_name)
        audio.write_audiofile(output_path)

        print(f"✅ MP3 saved: {output_path}")
    except Exception as e:
        print(f"❌ Conversion failed: {e}")
