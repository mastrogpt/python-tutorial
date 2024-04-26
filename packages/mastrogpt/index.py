#--web true
import json

def main(arg):
    data = {
        "services": [
            # add the demo entry, an object with name Demo and url mastrogpt/demo
            { 
                "name": "Demo", 
                "url": "mastrogpt/demo",
            },
            
        ]
    }
    return {"body": data}
