from pytube import YouTube
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

link = 'https://www.youtube.com/yourlink'

try:
    yt = YouTube(link)
    print('Please wait...')
    # QUALITY
    # audio_video = yt.streams.filter(res="1080p").first()
    # audio_video = yt.streams.filter(res="720p").first()
    # audio_video = yt.streams.filter(res="144p").first()

    # ONLY AUDIO
    # COMPRESSED
    # audio_video = yt.streams.filter(only_audio=True).first()
    # BEST QUALITY
    audio_video = yt.streams.get_audio_only()

    print('Downloading...')
    audio_video.download()

    print('Done!')

except Exception as e:
    print(f"An error occurred: {e}")
