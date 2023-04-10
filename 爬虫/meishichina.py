import requests
import json
import os
import time

def get_data(page):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }
    # 请求数据
    url = "https://home.meishichina.com/ajax/ajax.php"
    #目标网站有50页内容


    payload = {'ac': 'recipe',
                   'op': 'getMoreDiffStateRecipeList',
                   'classid': '0',
                   'orderby': 'hot',
                   'page': page}
        
    res = requests.get(url, headers=headers, params=payload)
    data_dict = json.loads(res.text)
    # print(res.text)
    with open('./美食/json/{}.json'.format(page),'w+', encoding='utf-8') as f:
        f.write(str(json.dumps(data_dict, indent=4)))
        print('成功写入第{}页'.format(page))
    
    # print(data)
   
    # for i in range(len(recipe)):
    #     name = recipe[i]["title"]
    #     imgurl = recipe[i]["fcover"]
    #     img = requests.get(imgurl,headers=headers)
    #refer设置有问题，目前无法爬取图片
    
        
    

        

    #h获取列表数据
        
if __name__ == "__main__":
    for i in range(1, 2):
        get_data(i)
        time.sleep(3)
