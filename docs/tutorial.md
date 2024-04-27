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

# Exercise 1 

### A function tht accepts `input` and return `output`

- `[1a]` Read the input  from the args

- `[1b]` Return the result as an dictionary: `{"output": output}`

  - remember to wrap the result in `{ "body" : ... }`

- `[1c]` Add the function to the index to use it...

---

# You can now chat with the function!

---

![bg](https://fakeimg.pl/350x200/ff0000,0/000?text=Using+OpenAI&retina=1)

---

xxx

---

![bg](https://fakeimg.pl/350x200/ff0000,0/000?text=Invoking+Completions&retina=1)

---

xxx
