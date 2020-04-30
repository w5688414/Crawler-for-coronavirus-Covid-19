from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm 

path='/usr/local/bin/chromedriver'

n=110

def get_page_source():
    
    browser = webdriver.Chrome(executable_path=path)
    
    try:
        url='https://www.nytimes.com/search?dropmab=false&endDate=20200426&query=Chinese+coronavirus&sort=best&startDate=20191126&types=article'
        browser.get(url)
        wait = WebDriverWait(browser, 20)
        for i in range(0, n):                  # n次点击加载更多
            print(i)
            # browser.find_element_by_xpath('//*[@id="site-content"]/div/div[2]/div[2]/div/button').click()  # 点击加载更多
            element = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="site-content"]/div/div[2]/div[2]/div/button')))
            # keyword.send_keys(Keys.ENTER)
            
            element.click()
            time.sleep(2)

        html=browser.page_source
    except Exception as e:
        html=browser.page_source
        print(e)

    finally:
        browser.close()
    return html

def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    liAll = soup.find_all('li', class_='css-1l4w6pd')
    list_data=[]
    for li in tqdm(liAll):
        news_name = li.find("h4", "css-2fgx4k").get_text()
        url=li.find("a").get('href')
        news_time=li.find("time",class_="css-17ubb9w")
        news_author=li.find("p","css-15w69y9")
        news_type=li.find('p','css-myxawk')
        # print(li)
        if(news_type):
            news_type=news_type.get_text()
        else:
            news_type=""
        # print(news_type)
        if(news_time):
            news_time=news_time.string
        else:
            news_time=""
        if(news_author):
            news_author=news_author.get_text()
        else:
            news_author=''
        if(url):
    
            print(url)
        else:
            url=""
        item_list=[news_time,news_author,news_name,url,news_type]
        # print(item_list)
        list_data.append(item_list)

    return list_data

def output_to_csv(list_data,csv_name):
    column_name = ['报道时间', '报道人','报道标题',"链接",'类型']
    xml_df = pd.DataFrame(list_data, columns=column_name)
    print(xml_df.shape)
    xml_df=xml_df.drop_duplicates()
    print(xml_df.shape)
    xml_df.to_csv(csv_name, index=None)


if __name__ == "__main__":
    html=get_page_source()
    with open('test.html','w') as f:
        f.write(html)
    list_data=get_data(html)
    output_to_csv(list_data,'new_york_times.csv')
