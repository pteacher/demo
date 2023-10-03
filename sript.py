from urllib.request import urlretrieve
from urllib.parse import urlparse
import os
import json
import git

URL = "http://185.68.22.253/api/v1/files"
file_name = os.path.basename(urlparse(URL).path)


def download(url):
    urlretrieve(url, file_name)


def run_file():
    os.system('python voice_gen.py')


def commit(repository: str):
    repo = git.Repo(repository)
    os.chdir(repository)
    try:
        repo.index.add('**')
        commit_message = f'voice_gen {file_name}'
        repo.index.commit(commit_message)
        print('Changes successfully added, committed, and pushed')
        origin = repo.remote(name='origin')
        origin.push()
    except Exception as e:
        print('An error occurred:', str(e))


if __name__ == '__main__':
    download(URL)
    repository_path = r'C:\Users\User\demo\.git'
    commit(repository_path)

    # copy from ..\voices\uni to \widget\public\voice
    # append to \widget\public\qa.js downloaded json
