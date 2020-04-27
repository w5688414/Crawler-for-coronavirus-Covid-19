from selenium import webdriver
import time
import os
import pandas as pd
from tqdm import tqdm 


path='/usr/local/bin/chromedriver'

def download_new_york_html(url_path,driver,root_path):
    driver.get(url_path)
    time.sleep(1)
    html_path=url_path.split('/')[-1]
    with open(os.path.join(root_path,html_path), 'w') as f:
        f.write(driver.page_source)

def download_new_york():
    root_path='html'
    csv_name='new_york_times_v2.csv'
    data=pd.read_csv(csv_name)
    driver = webdriver.Chrome(executable_path=path)
    for i in tqdm(range(data.shape[0])):
        url=data.iloc[i]['链接']
        url=url.split('?')[0]
        full_path='https://www.nytimes.com'+url
        print('download: '+full_path)
        download_new_york_html(full_path,driver,root_path)
    print("Done")
    driver.quit()


def download_wall_street_html(url_path,driver,root_path):
    html_path=url_path.split('/')[-1]+'.html'
    html_path=os.path.join(root_path,html_path)
    if(os.path.exists(html_path)):
            return 
    driver.get(url_path)
    time.sleep(1)
    with open(html_path, 'w') as f:
        f.write(driver.page_source)

def download_wall_street():
    root_path='html_wall_street'
    create_root(root_path)
    csv_name='The_Wall_Street_Journal.csv'
    data=pd.read_csv(csv_name)
    driver = webdriver.Chrome(executable_path=path)
    for i in tqdm(range(data.shape[0])):
        url=data.iloc[i]['链接']
        url=url.split('?')[0]
        full_path='https://www.wsj.com'+url
        print('download: '+full_path)
        download_wall_street_html(full_path,driver,root_path)
    print("Done")
    driver.quit()

def create_root(root_path):
    os.makedirs(root_path,exist_ok=True)


def download_washington_html(index,url_path,driver,root_path):
    html_path=str(index)+'.html'
    html_path=os.path.join(root_path,html_path)
    if(os.path.exists(html_path)):
        return
    driver.get(url_path)
    time.sleep(1)
    
    with open(html_path, 'w') as f:
        f.write(driver.page_source)

def download_washington_post():
    chrome_options = webdriver.ChromeOptions()
    # 设置代理
    # chrome_options.add_argument('--proxy-server=socks5://localhost:1080')
    root_path='html_washington'
    create_root(root_path)
    csv_name='washingtonpost.csv'
    data=pd.read_csv(csv_name)
    driver = webdriver.Chrome(executable_path=path)
    for i in tqdm(range(data.shape[0])):
        url=data.iloc[i]['链接']
        print('download: '+url)
        download_washington_html(i,url,driver,root_path)
    print("Done")
    driver.quit()




if __name__ == "__main__":
    # download_washington_post()
    download_wall_street()

    
