import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy , ProxyType
import time
import requests
import sys
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random
import re
from fake_useragent import UserAgent
from random import randint

    
def web():
    try:
        ## Rotating Requests through a pool of Proxies ##
        ua = UserAgent()
        proxies = []
        proxies_req = Request('https://www.sslproxies.org/')
        proxies_req.add_header('User-Agent', ua.random)
        proxies_doc = urlopen(proxies_req).read().decode('utf8')

        soup = BeautifulSoup(proxies_doc, 'html.parser')
        proxies_table = soup.find(id='proxylisttable')

        # Save proxies in the array
        for row in proxies_table.tbody.find_all('tr'):
            proxies.append({
            'ip':   row.find_all('td')[0].string,
            'port': row.find_all('td')[1].string
            })

        # Choose a random proxy
        proxy_index = random.randint(0, len(proxies) - 1)
        proxy = proxies[proxy_index]


        PROXY = proxy['ip'] + ':' + proxy['port']
        
        urls1 = ["https://lmlol.xyz","https://bot.lmlol.xyz","https://text.lmlol.xyz"]
        urls = random.choice(urls1)
        ##  urls  ##
        print("[+] URL : "+urls)
        print("[+] PROXY : "+PROXY)
        

        webdriver.DesiredCapabilities.CHROME['proxy'] = {
        "httpProxy": PROXY,
        "ftpProxy": PROXY,
        "sslProxy": PROXY,
        "proxyType":"MANUAL",
        }

        options = webdriver.ChromeOptions()
        ##hide debuge webdrive##
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument('headless')
        ua = UserAgent()
        options.add_argument(f'user-agent={ua.random}')
        options.add_argument("window-size=1400,600")
        headers = {'referer':'https://google.com/'}
        ##bot.lmlol.xyz##
        if "https://bot.lmlol.xyz" in urls: 
            with webdriver.Chrome(options=options , headers=headers) as driver:
                driver.get(urls)
                driver.implicitly_wait(5)
                if driver.find_element_by_id('root'):
                    print("[-] Finsh ")
                    print()
                driver.quit 
        ##lmlol.xyz##
        if "https://lmlol.xyz" in urls: 
            with webdriver.Chrome(options=options) as driver:
                driver.get(urls)
                driver.implicitly_wait(5)
                if driver.find_element_by_id('frmLogin'):
                    print("[-] Finsh ")
                    print()
                driver.quit  
        ##text.lmlol.xyz##
        if "https://text.lmlol.xyz" in urls: 
            with webdriver.Chrome(options=options) as driver:
                driver.get(urls)
                driver.implicitly_wait(5)
                if driver.find_element_by_id('content'):
                    print("[-] Finsh ")
                    print()
                driver.quit                                 
    except Exception as e: 
        print()
        print("[+] Restart")
        print()
while True:                          
    web()
    





