#--web true
def main(args):

    ## 1a read the input field from args in input, return '' as default
        
    # produce output from input with a suitable default
    input = "nothing" if input == "" else input
    output = { "output": f"You said: {input}" }

    #: 1b return a dictionary with key 'body' and value 
    return {
        "body": output 
    }
    
    #.
    
