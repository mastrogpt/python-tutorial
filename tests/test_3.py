# search for '## 3' in packages and solve issues

import os
import requests

import packages.openai.chat as chat

# this test checks you are connecting
def test_request():
    r = chat.request("2+2")
    assert r == [
        {'role': 'system', 'content': 'You are an helpful assistant.'},
        {'role': 'user', 'content': '2+2'}
    ]

    r = chat.request("2+2", "My Role")
    assert r[0]['content'] == "My Role"

def test_sum():
    host = os.environ["NUVDEV_HOST"]
    url = f"{host}/api/my/openai/chat"
    res = requests.post(url, json={"input": "2 + 2"}).json()
    print(res)
    assert res['output'].find("4") != -1
    