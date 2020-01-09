import subprocess
import shutil
import sys
import os

ARGS = sys.argv

if len(ARGS) < 2:
    exit('请设置无服务函数生成平台商!')

platform = ARGS[1]

if platform == 'aliyun':
    BASE_PATH = 'dist/aliyun'

if platform == 'tencent':
    BASE_PATH = 'dist/tencent'


def factoryPath(path: str) -> str:
    return os.path.join(BASE_PATH, path)


if platform == 'aliyun':
    shutil.copyfile('aliyun.py', factoryPath('index.py'))
    shutil.copyfile('reporting.py', factoryPath('reporting.py'))
    shutil.copyfile('private.json', factoryPath('private.json'))
    subprocess.run(['pip', 'install', '-r', 'requirements.txt', '-t', 'dist/aliyun'])

if platform == 'tencent':
    shutil.copyfile('tencent.py', factoryPath('index.py'))
    shutil.copyfile('reporting.py', factoryPath('reporting.py'))
    shutil.copyfile('private.json', factoryPath('private.json'))
    subprocess.run(['pip', 'install', '-r', 'requirements.txt', '-t', 'dist/tencent'])
