import youtube_dl

def download_subtitle(video_url):
    ydl_opts = {
        'writesubtitles': True,
        'subtitleslangs': ['en'],  # Change 'en' to the desired language code
        'skip_download': True,
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=False)
        if 'subtitles' in info:
            subtitles = info['subtitles']
            if subtitles:
                for lang, sub_info in subtitles.items():
                    if sub_info:
                        subtitle_url = sub_info[0]['url']
                        subtitle_text = ydl.urlopen(subtitle_url).read().decode('utf-8')
                        print(f'Subtitles for {lang}:')
                        print(subtitle_text)
                    else:
                        print(f'No subtitles available for {lang}')
            else:
                print('No subtitles available for this video')
        else:
            print('Subtitles not found')

# Replace 'VIDEO_URL' with the URL of the YouTube video
video_url = 'VIDEO_URL'
download_subtitle(video_url)
