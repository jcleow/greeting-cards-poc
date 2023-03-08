# Python Custom HTML + CSS Image Generator
POC to overlay images using python dom manipulation &amp; headless chromium wrapper

### How it works
* The idea is to create images using html + css using simple DOM manipulation.
* After which, we will use a headless browser to take a screenshot

### Rationale
* Using a framework as intensive as React when there isn't much state mangement to handle, nor are there any re-rendering of any DOM elements. Hence we probably don't need these additional overheads for such use case.
* We can easily port it into a python backend to generate such images as a background job.

### How to Run
Set up your environment first with a pyenv virtualenv. I used 3.10.6 out of convenience


```
pyenv virtualenv  3.10.6 venv310greetingscard
pip install dominate
pip install html2image
python create_greeting_card.py
```

** Make sure you have Chrome installed (html2image uses Chromium) **

See these github libraries here:
* https://github.com/Knio/dominate/ [~1.5k stars | Seems like it is a stable version already]
* https://github.com/vgalin/html2image [199 stars | 3.0 Alpha Build]

### Additional Steps for using html2page:
html2page is an alpha build version so there are some small bugs here and there
1. Be sure to change the url to an absolute one(in dev/prod we can just use a url) locally
2. html2Page also has some documentation on how to deploy onto docker, so it would be interesting to check that out as well.

### Known errors
```[0307/230411.724353:ERROR:command_buffer_proxy_impl.cc(128)] ContextResult::kTransientFailure: Failed to send GpuControl.CreateCommandBuffer.``` comes from html2page. Not sure why its happening

### Other Considerations/next steps:
1. We can also investigate using [playwright](https://github.com/microsoft/playwright-python) but havent gotten a chance to.

Alternative was pyppeteer[https://github.com/pyppeteer/pyppeteer] but seems outdated. This is because html2page is still an alpha build, but it is really easy to use

2. Instead of using dominate, I wanted to try using [pyscript](https://pyscript.net/) but it seems to be in alpha stage as well. But its not a big deal since dominate seems to work fine.




