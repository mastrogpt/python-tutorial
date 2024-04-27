
# search for '## 2' in packages and solve issues

import os, requests
import packages.openai.chat as chat
import packages.mastrogpt.index as index

def test_welcome():
    host = os.environ["NUVDEV_HOST"]
    url = f"{host}/api/my/openai/chat"
    res = requests.get(url).json()
    print(res)
    assert res['output'] == "Welcome."

def test_index():
    entry = index.main({})["body"]["services"][1]
    assert entry["name"] == "OpenAI"
    assert entry["url"] == "openai/chat"
