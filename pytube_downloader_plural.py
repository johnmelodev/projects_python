from pytube import YouTube
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

links = [
    'https://www.youtube.com/watch?v=mPZkdNFkNps&t=1268s',
    'https://www.youtube.com/watch?v=5DcTSjjO7mA&t=12812s'
]

try:
    for link in links:
        yt = YouTube(link)
        print(f'Processing link: {link}')

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

        print(f'Done downloading from {link}\n')

except Exception as e:
    print(f"An error occurred: {e}")
