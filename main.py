import yt_dlp

def download_youtube_video(video_url):
    save_path = './'  # Projektordner
    try:
        ydl_opts = {
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',  # Speichert im Projektordner
            'format': 'bestvideo+bestaudio/best',         # Beste Video- und Audioqualität
            'merge_output_format': 'mp4',                # Zusammenführen in MP4-Format
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print("Download completed!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ").strip()
    download_youtube_video(video_url)
