import fire
from bs4 import BeautifulSoup
import urllib
from urllib.request import Request, urlopen, urlretrieve
import re

def dl_until_size(links_file, size):
    with open(links_file) as f:
        links = f.readlines()

    # Test
    with open('test.ly', 'w') as f:
        f.write(urlopen(links[0]).read().decode('utf-8'))

def cli():
    fire.Fire(dl_until_size)
