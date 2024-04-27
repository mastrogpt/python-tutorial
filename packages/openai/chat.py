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

def connect(args):
    ## 3a connect ai with Azure OpenAI
    pass

def main(args):
    # connect to the AI
    ai = connect(args)

    # read input and produce output
    input = args.get("input", "")

    output = ""
    ## 3d define the default message 'Welcome.'

    if input != "":
        output = ask(ai, input)

    # return the result
    return {
        "body": { "output": output}
    }
