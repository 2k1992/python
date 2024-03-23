from pytube import YouTube

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
        if stream:
            print("Downloading:", yt.title)
            stream.download(output_path=save_path)
            print("Download complete!")
        else:
            print("No progressive stream available for this video.")
    except Exception as e:
        print("Error:", e)

def main():
    url = input("Enter the YouTube video URL: ")
    save_path = input("Enter the directory where you want to save the video: ")

    download_video(url, save_path)

if __name__ == "__main__":
    main()

