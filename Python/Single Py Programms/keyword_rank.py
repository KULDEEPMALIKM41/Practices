import bs4

import requests, time
import html2text
page = 0
file=""
count=0
list=[]
headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

for i in range(10):
    url = "https://www.google.co.in/search?q=seo+company&start="+str(page)
    data = requests.get(url)
    soup = bs4.BeautifulSoup(data.text, 'html.parser')
    # struct_html = soup.prettify()
    paras = soup.find_all('a')

    for para in paras:
        link = para.get("href")
        if link.startswith("/url?q="):
            count += 1
            actual_link = link.replace("/url?q=", "")
            indx = actual_link.find("&sa=")
            fltr_link = actual_link.replace(str(actual_link[indx:len(actual_link)]),"")
            try:
                data2 = requests.get(fltr_link, headers=headers, stream=True, verify=False, timeout=600)
                soup2 = bs4.BeautifulSoup(data2.text, 'html.parser')
                h2t = soup2.prettify()
                filedata=html2text.html2text(h2t)
                file=file+str(filedata).lower()
                if count%10 == 0:
                    list.append(file.count("seo company"))
                    file=""

            except Exception as e:
                print(e)
            print(count, "Request Completed...wait, status ",data2," url : ",fltr_link)
            if count%10 == 0:
                break
    page += 10
print("\n All requests are completed \n")
page2 = 1
for i in list:
    print(i," Keywords on page ",page2)
    page2 += 1




# try:
# 	from googlesearch import search
# except ImportError:
# 	print("No module named 'google' found")
# 
# http_proxy  = "http://10.10.1.10:3128"
# https_proxy = "https://10.10.1.11:1080"
# ftp_proxy   = "ftp://10.10.1.10:3128"
# 
# proxyDict = {
#               "http"  : http_proxy,
#               "https" : https_proxy,
#               "ftp"   : ftp_proxy
#             }
# 
# headers = {
#                 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
# query = "seo company"
# try:
#     c=1
#     file=""
#     list=[]
#     for j in search(query,  num=1, stop=100.0, pause=5):
#         data = requests.get(j, headers=headers, stream=True, verify=False, timeout=600)
#         soup = bs4.BeautifulSoup(data.text, 'html.parser')
#         h2t = soup.prettify()
#         filedata=html2text.html2text(h2t)
#         file=file+str(filedata).lower()
#         if c%10 == 0:
#             list.append(file.count("seo company"))
#             file=""
#         print(c ,"Request Completed...wait")
#         c += 1
# 
#     for i in list:
#         print(i)
# 
# except Exception as e:
#     print(e)