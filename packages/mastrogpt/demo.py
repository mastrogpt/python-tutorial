#--web true
def main(args):

    # read the input field from args in input, return '' as default
    input = args.get("input", "")
    
        
    # produce output from input with a suitable default
    input = "nothing" if input == "" else input
    output = { "output": f"You said: {input}" }

    # return a dictionary with key 'body' and value 
    return {
        "body": output 
    }
    
    
