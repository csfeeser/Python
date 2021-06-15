# Let's Try Webscraping!

<img src="https://thumbs.dreamstime.com/b/samurai-katana-sword-sakura-flowers-vector-design-set-traditional-scabbard-blossom-japanese-warrior-blade-cherry-159438168.jpg" alt="drawing" width="200"/>

Using the tools/scripts that you've been shown with [Beautiful Soup](https://github.com/csfeeser/Python/blob/071f58160babb4568091a8eb0223070b52d88931/TLG/webscraping.md), attempt your own webscrape!

Choose between one of the two websites below:

- [300 Flower Names and Types with Pictures](https://florgeous.com/types-of-flowers/)

- [The Epic List of 250 Legendary Swords](https://hobbylark.com/fandoms/The-Epic-List-of-250-Legendary-Swords)

In both sites, you're presented with a long list of data (names of flowers or swords) as well as a description of each item. Using Beautiful Soup, return ALL the flowers/swords AND THEIR DESCRIPTIONS from the page and place them inside of a dictionary. The format of the dictionary is up to you- what do you think will be the best design?

<!--
#!/usr/bin/python3
"""
Learning to scrape webdata with BeautifulSoup
"""

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from bs4 import element
import json

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            # stream=True means Requests cannot release the connection until closed
            # closing() will close "resp" at the end of this block
            if is_good_response(resp):
                return resp.content
                # .content() reads the HTML of the Requests object
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)

'''
return dictionary of flowers with key: name and value: description
'''
def readFlowers(url):
    raw_html = simple_get(url)
    html = BeautifulSoup(raw_html, 'html.parser')
    flowers = {}
    for h3 in html.select("h3"):
        if not h3.is_empty_element:
            id = h3.get('id')
            if not id == None:
                desc = h3.find_next_sibling('p')
                flowers[h3.text] = desc.text
    return flowers

def main():
    flowers = readFlowers('https://florgeous.com/types-of-flowers/')
    with open("/home/student/static/flowersuccess.json","w") as flowerfile:
        json.dump(flowers, flowerfile)

if __name__ == "__main__":
    main()
-->
