yt-dlp \
    -s \
    --write-description \
    --print-to-file \
    "%(title)s;%(upload_date)s;http://youtu.be/%(id)s;%(duration)s;%(tags)l" \
    lives.csv \
    https://www.youtube.com/@Dunossauro/streams
