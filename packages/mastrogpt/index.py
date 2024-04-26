#--web true
import json

def main(arg):
    data = {
        "services": [
            ## 1c add the demo entry, an object with name Demo and url mastrogpt/demo
            
            ## 2b add the OpenAI entry, an object with name Demo and url mastrogpt/demo
        ]
    }
    return {"body": data}
