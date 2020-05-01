import requests
from Config import *
import os


def bulk_download(download_details, destination):
    try:
        for value in download_details.values():
            download_file(value["download_url"], destination + "/" + value["file_name"])
    except KeyError:
        print("Encountered key error, check spellings")


def download_file(url, path):
    headers = { 'User-Agent': '\''+ user_agent + '\''}
    file = requests.get(url, headers=headers)
    write_file(file, path)


def write_file(file, path):
    try:
        if not os.path.exists(destination):
            os.makedirs(os.path.dirname(path))
        open(path, 'wb').write(file.content)
    except IOError:
        print("Io error while writing file : " + path)
