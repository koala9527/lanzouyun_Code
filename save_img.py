import requests
urls = "https://vip.d0.baidupan.com/file/imagecode.php"

for i in range(100):
    datas = requests.get(urls)
    with open('./verify/'+str(i)+'.png', 'wb') as file:
        file.write(datas.content)