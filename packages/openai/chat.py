#--web true
#--param OPENAI_API_HOST $OPENAI_API_HOST
#--param OPENAI_API_KEY $OPENAI_API_KEY
#--kind python:default

from openai import AzureOpenAI

ROLE = "You are an helpful assistant."
MODEL = "gpt-35-turbo"

def request(input, role=ROLE):
    ## 3a generate the role as shown in test3.test_request
    pass

def ask(ai, input, role=ROLE):
    
    comp = None
    ## 3b invoke the chat completion API
    
    res = "Sorry, there is an error"
    
    ## 3c read the first message content if any
        
    return res

def connect(args):
    pass
    ## 2a connect ai with Azure OpenAI and return the api object

def main(args):
    # connect to the AI
    ai = connect(args)

    # read input and produce output
    input = args.get("input", "")

    output = "Connection Error."
    ## 2b if the connection is not closed, return 'Welcome.'

    # if the input is not empty, ask to the AI
    if input != "":
        output = ask(ai, input)

    # return the result
    return {
        "body": { "output": output}
    }
