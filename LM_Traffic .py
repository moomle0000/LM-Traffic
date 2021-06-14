 from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import csv


def login(PROXY,keyword,urls):
    options = webdriver.ChromeOptions()
    options.add_argument('--proxy-server=%s' % PROXY)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
            
    with webdriver.Chrome(options=options) as driver:

        print("[+] Google Search : "+keyword)
        driver.get('https://www.google.com/search?q='+keyword)
        time.sleep(6)
        driver.get(urls)
        print("[+] url : "+urls)
        print("[+] keyword : "+keyword)
        print("[+] Proxy : "+PROXY)
        print()
        time.sleep(10)
        driver.quit

count = 0
count1 = 0
count2 = 0
while True:

    lines1 = [line for line in open ("proxy.txt")]

    count += 1
    PROXY = lines1[count].strip()


    lines2 = [line for line in open ("urls.txt")]

    count1 += 1
    urls = lines2[count].strip() 

    lines3 = [line for line in open ("keyword.txt")]

    count2 += 1
    keyword = lines3[count].strip() 

    try:
        
        login(PROXY,keyword,urls)
        
    except:
        print()
        print("[+] Restart")
        print()
        continue
