from pytube import YouTube


def download_mp4_videos(url: str, quality: str):
    try:
        youtube = YouTube(url)
        youtube.streams.filter(file_extension="mp4").get_by_resolution(quality).download()
        print("Download is successful")
    except Exception:
        print("Check the url!!!")


qualities = {1: "360p",
             2: "480p",
             3: "720p",
             4: "1080p"}

url = input("Enter a valid Youtube video url:\n")
level = int(input("Enter a quality level(1-4):\n"))
quality = qualities[level] if 1 <= level <= 4 else qualities[1]
download_mp4_videos(url, quality)
