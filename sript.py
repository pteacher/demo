from urllib.request import urlretrieve
from urllib.parse import urlparse
import os
import json
import yaml
import git

URL = "http://185.68.22.253/download/mrartur0074githubio64fdc95c69c9f.yaml"
file_name = os.path.basename(urlparse(URL).path)


# json_dir = r'D:\projects\venv\old_conv'


def download(url):
    urlretrieve(url, file_name)


def parse_yaml_json(file: str):
    with open(file, 'r', encoding='utf-8') as yaml_file:
        data_yaml = yaml.safe_load(yaml_file)

    with open(f"{file.split('.')[0]}.json", 'w', encoding='utf-8') as json_file:
        json.dump(data_yaml, json_file, indent=4, ensure_ascii=False)


download(URL)
parse_yaml_json(file_name)
# os.system('python voice_gen.py')

# copy from ..\voices\uni to \widget\public\voice
# append to \widget\public\qa.js downloaded json
repository_path = r'C:\Users\User\demo\.git'
commit_message = f'voice_gen {file_name}'
repo = git.Repo(repository_path)
os.chdir(repository_path)

try:
    repo.index.add('**')
    repo.index.commit(commit_message)
    print('Changes successfully added, committed, and pushed')
    origin = repo.remote(name='origin')
    origin.push()
except Exception as e:
    print('An error occurred:', str(e))

if __name__ == '__main__':
    pass
