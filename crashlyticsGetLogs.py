#!/usr/bin/python
import requests
from BeautifulSoup import BeautifulSoup
import re
import json
import config
#TODO iterate through the links
payload = config.payload
login_url= 'https://fabric.io/api/v2/session'
link = config.link
url = 'https://fabric.io/login'
with requests.Session() as client:
    client.headers.update({'User-Agent':   'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0'})
    resp = client.get(url)
    soup = BeautifulSoup(''.join(resp.text))
    csrf_token = soup.findAll('meta')[2]['content']
    client.headers.update({'X-CSRF-Token': csrf_token})
    
    print client.headers
    print csrf_token
    p = client.post(login_url, data=payload)
    print client.cookies

    first_pass = True
    while(first_pass or response.status_code == 200):
        first_pass = False

        response = client.get(link )
        filename = response.url.rsplit('/',1)

        print('Saving JSON data for session '+filename[-1])
        filename = filename[-1]+'.txt'
        f = open(filename, 'w')

        json.dump(response.json(), f)

        prev = response.links['prev']['url']
        link = prev


