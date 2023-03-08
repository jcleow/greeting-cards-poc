import time
import dominate
from dominate.tags import *
import time
from html2image import Html2Image


start = time.time()
# 1. Use dominate to perform DOM manipulation
doc = dominate.document(title='Dominate your HTML')

with doc.head:
    link(rel='stylesheet', href='greeting_card.css')

@div
def agent_profile_pic(agent_info: dict):
    image = img()
    image["src"] = agent_info.get("profile_pic_url")


@div(cls="agentDetails")
def agent_details(agent_info: dict):
    span(agent_info.get("name"))
    br()
    span(agent_info.get("contact_num"))
    br()
    span(f"{agent_info.get('agency_name')} | CEA: {agent_info.get('cea_num')}")


@div(cls="agentSection")
def agent_info_section(agent_info: dict):
    agent_profile_pic(agent_info)
    agent_details(agent_info)



@div(cls="template")
def greeting_card_template():
    image = img()
    # Have to use absolute path for testing locally on HTML2Image; in our app we can just use a URL
    # See: https://github.com/vgalin/html2image/issues/47
    image["src"] = "/Users/jitcorn/Desktop/99_custom_scripts/greeting-cards-poc/easter.png"


with doc:
    with div(cls="container"):
        # mock agent info here
        agent_info = {
            "name":  "Jessica Tan Xin Yi",
            "contact_num": "987654321",
            "agency_name": "PROPNEX REALTY PTE. LTD.",
            "cea_num": "R042395I",
            # Have to use absolute path for testing locally on HTML2Image; in our app we can just use a URL
            # See: https://github.com/vgalin/html2image/issues/47
            "profile_pic_url": "/Users/jitcorn/Desktop/99_custom_scripts/greeting-cards-poc/agent_profile.png"
        }
        agent_info_section(agent_info)
        greeting_card_template()

with open("greeting_card.html", 'w') as f:
    f.write(str(doc))

# 2. Use HTML2Image (a wrapper on a headless browser -default is Chromium browser) to perform screenshot
# Set this size to be the exact size of the greeting that we have because they don't have the feature to auto identify image
hti = Html2Image(size=(687,1220))
hti.screenshot(html_file="greeting_card.html", css_file="greeting_card.css", save_as='greeting_card.png')

end = time.time()
print(f'Took {end-start} seconds')





