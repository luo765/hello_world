import json
import os
import requests
basepath =os.getcwd()

headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }

for i in range(1, 10):
    path = "./美食/json/{}.json".format(i)

    try:
        with open(path, 'r', encoding = 'utf-8') as f:
            file_dict = json.loads(f.read())#有32个
            data_dict = file_dict["data"]
            for j in data_dict:
                title = j["title"]
                mainingredient= j["mainingredient"]
                imgurl = j["fcover"].split("?")[0]

                fileend = imgurl.split(".")[-1]


                if os.path.exists(os.path.join(basepath, '美食', '菜品名字', title)):
                    print("文件夹已经存在")
                else:
                    r = requests.get(imgurl,headers=headers)
                    print(r.status_code)
                    os.mkdir("./美食/菜品名字/{}".format(title))

                    with open("./美食/菜品名字/{}/{}.{}".format(title, title, fileend),'wb') as f:
                        f.write(r.content)
                        print("{} picture success ".format(title))
                    with open("./美食/菜品名字/{}/{}.txt".format(title, title),'w+', encoding='utf-8') as f:
                        f.write(str(j))
                        print("{} txt success".format(title))
    

    except:
        print('第{}页出现问题'.format(i))
    finally:
        pass

                               
                                       
                                   
                                   
                                   
                                   
                                       
                                       
                
    

