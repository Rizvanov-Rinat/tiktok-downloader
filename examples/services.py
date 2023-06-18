import requests

from tiktok_downloader import services, InvalidUrl


def download(url: str, video_name: str):
    for service in services.values():
        try:
            media = service(url)
        except (InvalidUrl, requests.exceptions.InvalidURL, IndexError, ValueError) as e:
            print(f'Error with {url} in {service.__name__}: {e}')
        else:
            if media:
                media[0].download(video_name)
                print(f'{video_name} successfully downloaded.')
                return
    print(f'Unable to download media from {url} with any available service.')


if __name__ == "__main__":
    url = "<TIKTOK URL>"
    video_name = "example.mp4"
    download(url, video_name)
