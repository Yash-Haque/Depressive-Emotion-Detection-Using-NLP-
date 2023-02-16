import os
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions as EC

def main():
  
    os.environ['PATH'] += r"C:/SeleniumDrivers"
    s=Service("C:\\SeleniumDrivers\\msedgedriver.exe")
    driver = webdriver.Edge(service=s)

    record = []
    url = "https://www.reddit.com/r/depression/"
    c=0
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html-parser')
    results = soup.find_all('div', {'class':'_1oQyIsiPHYt6nx7VOmd1sz _1RYN-7H8gYctjOQeL8p2Q7 scrollerItem _3Qkp11fjcAw9I9wtLo8frE _1qftyZQ2bhqP62lbPjoGAh  Post t3_10x73qw '})
    is_moderator = i.find_all('div',{'class':'_3vju76MdF2FaGmELBeiJ_r _SMl46gACTEszA_4A0Qfs icon icon-mod_fill'})
    for i in results:
        if record (is_moderator and c<3):
            continue
        else:
            record=extract_record(i)
            c+=1

    print(results)
    driver.close()
    


def extract_record(i):
    post = i.find_all('div', {'class':'_1poyrkZ7g36PawDueRza-J _11R7M_VOgKO1RJyRSRErT3 '})
    for j in post:
        username=j.a
        post_title=j.a.h3
    result = (username, post_title)
    return result

main()
