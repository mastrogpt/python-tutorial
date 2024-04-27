---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.jpg')
html: true
---

![bg left:40% 80%](./logo-full-transparent.png)

# **MastroGPT Training**
## Implementing a Chatbot with Nuvolaris


https://www.nuvolaris.io

---

![bg](https://fakeimg.pl/350x200/ff0000,0/000?text=Serverless+Functions&retina=1)

---

# What is a serverless function?

- a Python (or other languages) source code

  - Single file or multi file

- Receives a `dict` as input and returns a `dict` as output

    - If it is a web actions, it produces HTML, JSON or others

    - You need to wrap the output in the `body` field:

```
{ "body": "<h1>Hello</h1>"}
```

--- 
# Implementing a simple chat

### A function tht accepts `input` and return `output`

- `[1a]` Read the input  from the args

- `[1b]` Return the result as an dictionary: `{"output": output}`

  - remember to wrap the result in `{ "body" : ... }`

- `[1c]` Add the function to the index to use it...

### You can chat with the function!

---

![bg](https://fakeimg.pl/350x200/ff0000,0/000?text=Using+OpenAI&retina=1)

---
# Connecting to OpenAI

```python
from openai import AzureOpenAI
 
ver = "2023-12-01-preview"
# key and host provided by MastroGPT
key = args.get("OPENAI_API_KEY")
host = args.get("OPENAI_API_HOST")
# api call
ai =  AzureOpenAI(
    api_version=ver, 
    api_key=key, 
    azure_endpoint=host)
```

- `[2a]` connect ai with Azure OpenAI and return the api object


---
# Ckecking the connection

```python
# retrieve informations about a model
MODEL = "gpt-35-turbo"
model = ai.models.retrieve(MODEL)
# if ok model.status == 'succeded'
```

- `[2b]` retrieve the model we use, check the status  and return 'Welcome.' if is 'succeeded'

- `[2c]` add the new chat to the indes

## Chat with it and verify you get `Welcome`
---

![bg](https://fakeimg.pl/350x200/ff0000,0/000?text=Chat+with+GPT&retina=1)

---
## Create a request

Structure of a request:

```python
[
   {"role": "system", "content": ROLE},
   {"role": "user", "content": input}
] 
```

- `[3a]` a function to return a request

---

## Invoke a request and return the result

```python
comp = ai.chat.completions.create(
    model=MODEL, 
    messages=request(input, role)
)
```
- `[3b]` invoke the chat completion API

```python
res = comp.choices[0].message.content
```

 - `[3c]` read the first message content if any

### Now you can chat with the AI