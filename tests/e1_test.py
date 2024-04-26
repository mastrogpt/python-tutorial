# search for '## 1' and solve issues

import packages.mastrogpt.demo as demo
import packages.mastrogpt.index as index

def test_demo():
    # Expect result: 
    # {
    #   "body": "You said: nothing"
    # }
    assert demo.main({})["body"] == "You said: nothing"
    # Expect result:
    # {
    #   "body": "You said: hello"
    # }
    assert demo.main({"input": "hello"})["body"] == "You said: hello"

def test_index():
    # Expect result:
    # {
    #   "body": {
    #      "services": {
    #           "name": "Demo",
    #           "url": "mastrogpt/demo" 
    #       }
    #    }
    # } 
    entry = index.main({})["body"]["services"][0]
    assert entry["name"] == "Demo"
    assert entry["url"] == "mastrogpt/demo"
