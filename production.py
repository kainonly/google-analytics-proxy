import subprocess
import shutil
import sys
import os

ARGS = sys.argv

if len(ARGS) < 2:
    exit('Please set serverless platform provider!')

platform = ARGS[1]

if platform == 'aliyun':
    BASE_PATH = 'dist/aliyun'

if platform == 'tencent':
    BASE_PATH = 'dist/tencent'


def factoryPath(path: str) -> str:
    return os.path.join(BASE_PATH, path)


if platform == 'aliyun':
    shutil.copyfile('platform/aliyun.py', factoryPath('index.py'))
    shutil.copyfile('reporting.py', factoryPath('reporting.py'))
    shutil.copyfile('private.json', factoryPath('private.json'))
    subprocess.run(['pip', 'install', '-r', 'requirements.txt', '-t', 'dist/aliyun'])

if platform == 'tencent':
    shutil.copyfile('platform/tencent.py', factoryPath('api_service.py'))
    shutil.copyfile('reporting.py', factoryPath('reporting.py'))
    shutil.copyfile('private.json', factoryPath('private.json'))
    subprocess.run(['pip', 'install', '-r', 'requirements.txt', '-t', 'dist/tencent'])
