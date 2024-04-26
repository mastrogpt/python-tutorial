# search for '## 1' in packages and solve issues

import packages.mastrogpt.demo as demo
import packages.mastrogpt.index as index

def test_demo():
    # expected result: 
    # {
    #   "body": { "output": "You said: nothing" }
    # }
    assert demo.main({})["body"] == "You said: nothing"

    # expected result:
    # {
    #   "body": { "output": "You said: hello" }
    # }
    assert demo.main({"input": "hello"})["body"] == "You said: hello"

def test_index():
    # expected result:
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
