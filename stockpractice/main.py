import os
import time
import fitz
import requests


#
# doc = fitz.open("./test.pdf")
#
# print(len(doc) )
# page = doc.loadPage(0)
# text = page.getText()
#
# print(text)
#
# total_text =""
#
# for i in doc:
#     total_text = total_text+i.getText()
#
# file = open("./total_text.txt",'wb')
# file.write(total_text.encode("UTF-8"))
# file.close()

file = open("./total_text.txt",'rb')
lines = file.readlines()
file.close()

last_list = list()
temp =""

for i in lines:
    i = i.decode("UTF-8")
    i = i.replace("\n"," ")

    if len(temp + i)>5000:
        last_list.append(temp)
        temp =""
    else:
        temp = temp+i

print(len(last_list))

request_url = "https://openapi.naver.com/v1/papago/n2mt"
headers = {"X-Naver-Client-Id":"Ucbjhq7NFh3QAtoTWBQS", "X-Naver-Client-Secret": "mueqwp9q6Y"}
params = {"source": "en", "target":"ko","text": last_list[0]}
response = requests.post(request_url,headers=headers, data= params)
result = response.json()

print(result)
print(result['message']['result']['translatedText'])

file = open("./trans.txt",'wb')
file.write(result['message']['result']['translatedText'].encode("UTF-8"))
file.close()


# path_dir = "C:\\Users\\Kim\\test"
# file_list = os.listdir(path_dir)
#
# print(file_list)
#
# image_list = list()
#
# for i in file_list:
#     try:
#         if i.split(".")[1] =="jpg" or i.split(".")[1] == "png":
#             image_list.append(i)
#     except Exception as error:
#         print(error)
#
# print(image_list)
#
# get_time = os.path.getmtime(path_dir+"\\"+image_list[0])
# print(get_time)
#
# time.localtime(get_time)
#
# file_data = time.strftime("%YY %mM %dD _ %HH %MM",time.localtime(get_time))
# print(file_data)
#
# print(type(file_data))

