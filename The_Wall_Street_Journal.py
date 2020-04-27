from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm 
from time import sleep

path='/usr/local/bin/chromedriver'


def get_page_source(browser,page_num=0):

    try:
        url='https://www.wsj.com/search/term.html?KEYWORDS=coronavirus&source=wsjarticle&isAdvanced=true&daysback=90&page={}'.format(page_num)
        browser.get(url)
        wait = WebDriverWait(browser, 10)
        element = wait.until(EC.element_to_be_clickable((By.ID,'search-results')))
        html=browser.page_source
    except Exception as e:
        print(e)
        return
    # finally:
    #     browser.close()
    return html

def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    print(html)
    liAll = soup.find_all('li',attrs={"xmlns": "http://www.w3.org/1999/html"})
    # print(liAll)
    list_data=[]
    for li in tqdm(liAll):
        # print(li)
        news_name = li.find("h3", "headline").get_text()
        # print(news_name)
        url=li.h3.a.get('href')
        # print(url)
        article_info=li.find("div","article-info")
        # print(article_info)
        author=article_info.find("li",'byline')
        if(author):
            author=author.find('span').get_text()
        else:
            author=""
        # print(author)

        news_time=article_info.find('time').get_text()
        # print(news_time)

        category=li.find('div',"category").get_text()
        item_list=[news_time,author,news_name,url,category]
        print(item_list)
        list_data.append(item_list)

    return list_data

def output_to_csv(list_data,csv_name):
    column_name = ['报道时间', '报道人','报道标题',"链接",'类型']
    xml_df = pd.DataFrame(list_data, columns=column_name)
    xml_df.to_csv(csv_name, index=None)


if __name__ == "__main__":
    browser = webdriver.Chrome(executable_path=path)
    list_res=[]
    for i in range(100):
        html=get_page_source(browser,i)
        with open('test.html','w') as f:
            f.write(html)
        list_data=get_data(html)
        list_res+=list_data
    browser.close()
    output_to_csv(list_res,'The_Wall_Street_Journal.csv')
