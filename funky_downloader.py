import bs4 as bs
import urllib.request
import tldextract
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



def page_round_up() -> str:
    source = urllib.request.urlopen('https://www.unknown.notreal.com').read()
    soup = bs.BeautifulSoup(source,'lxml')
    url_list=[]
    for link in soup.findAll('a', {'class': 'brownBtn'}):
        try:
            x = link['href']
            url_list.append(x)
        except KeyError:
            pass
    return url_list

def page_breakdown_url(url_list:str) -> str:
        page_sub_list = []
        for urls in url_list:
            source = urllib.request.urlopen(urls).read()
            soup = bs.BeautifulSoup(source,'lxml')
            
            for source in soup.find_all('a', href=True):
            #    print ("Found the URL:", source['href'])

                x = tldextract.extract(source['href'])
                if x.domain == 'easybytez':
                    url = source['href']
                    page_sub_list.append(url)
        return page_sub_list


def download_url(url: str):
    driver = webdriver.Chrome('./chromedriver')
    driver.get(url)
    time.sleep(5)
    arrow = driver.find_element(By.NAME, "method_premium").click()
    time.sleep(5)
    driver.close
    
if __name__ == "__main__":
    url_list = page_round_up()  
    urls = page_breakdown_url(url_list)
    for url in urls:  
        print(url)
    


