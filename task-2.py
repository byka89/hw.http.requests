import requests

TOKEN = ""


def get_dl_url(path):
    url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
    headers = {"Authorization": TOKEN}
    params = {"path": path, "overwrite": "true"}
    response = requests.get(url, headers=headers, params=params)
    return response.json()["href"]


def write_file_yd(download_link, file_link):
    data = open(file_link, "rb")
    href = get_dl_url(download_link)
    response = requests.put(href, data)
    response.raise_for_status()
    if response.status_code == 201:
        print("Uploaded")


write_file_yd("/tests/file.txt", r"/home/alex/Desktop/Projects/file.txt")