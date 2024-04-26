
# search for '## 2' in packages and solve issues

import packages.openai.chat as chat
import packages.mastrogpt.index as index


def test_request():
    r = chat.request("2+2")
    assert r == [
        {'role': 'system', 'content': 'You are an helpful assistant.'},
        {'role': 'user', 'content': '2+2'}
    ]

    r = chat.request("2+2", "My Role")
    assert r[0]['content'] == "My Role"

def test_index():
    entry = index.main({})["body"]["services"][1]
    assert entry["name"] == "OpenAI"
    assert entry["url"] == "openai/chat"



