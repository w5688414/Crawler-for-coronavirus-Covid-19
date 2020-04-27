import os 
import time
from tqdm import tqdm
import pandas as pd
import json

def read_json(json_path):
    with open(json_path,'r') as load_f:
        load_dict = json.load(load_f)
    return load_dict

def parse(load_dict):
    articles=load_dict['results']['documents']
    list_data=[]
    for article in tqdm(articles):
        # print(article)
        news_url=article['contenturl']
        if('byline' not in article):
            continue
        if('primarysection' in article):
            news_type=article['primarysection']
        else:
            news_type=article['byline']
        news_title=article['mobileheadline']
        
        news_author=article['byline']
        timeStamp = article['displaydatetime']/1000
        timeArray = time.localtime(timeStamp)
        otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
        list_data.append([otherStyleTime,news_author,news_title,news_url,news_type])
    return list_data



def output_to_csv(list_data,csv_name):
    column_name = ['报道时间', '报道人','报道标题',"链接",'类型']
    xml_df = pd.DataFrame(list_data, columns=column_name)
    print(xml_df.shape)
    xml_df=xml_df.drop_duplicates()
    print(xml_df.shape)
    xml_df.to_csv(csv_name, index=None)

if __name__ == "__main__":
    json_root='./data'
    json_files=os.listdir(json_root)
    list_res=[]
    json_files=[item for item in json_files if(item.split('.')[-1]=='json')]
    for item in json_files:
        json_path=os.path.join(json_root,item)
        print(json_path)
        load_dict=read_json(json_path)
        list_data=parse(load_dict)
        list_res+=list_data
    csv_name='washingtonpost.csv'
    output_to_csv(list_res,csv_name)
    print('Done')