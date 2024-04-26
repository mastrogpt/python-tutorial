#--web true
#--param OPENAI_API_HOST $OPENAI_API_HOST
#--param OPENAI_API_KEY $OPENAI_API_KEY
#--kind python:default

from openai import AzureOpenAI

ROLE = "You are an helpful assistant."
MODEL = "gpt-35-turbo"

def request(input, role=ROLE):
    ## 2a generate the role as shown in test2.test_request
    pass

def ask(ai, input, role=ROLE):
    
    comp = None
    ## 3b invoke the chat completion

    res = "Sorry, there is an error"
    ## 3c read the first message content if any
    
    return res

def main(args):
    ai = None
    ## 3a connect ai with Azure OpenAI

    # read input and produce output
    input = args.get("input", "")
    output = ask(ai, input)
    return {
        "body": { "output": output}
    }
