# search for '## 3' in packages and solve issues

import os
import requests
import json

import packages.openai.chat as chat

def test_welcome():
    host = os.environ["NUVDEV_HOST"]
    url = f"{host}/api/my/openai/chat"
    res = requests.get(url).json()
    print(res)
    assert res['output'] == "Welcome."

def test_sum():
    host = os.environ["NUVDEV_HOST"]
    url = f"{host}/api/my/openai/chat"
    res = requests.post(url, json={"input": "2 + 2"}).json()
    print(res)
    assert res['output'].find("4") != -1
    