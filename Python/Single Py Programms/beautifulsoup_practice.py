import bs4

import requests
url = "https://www.facebook.com/kuldeep.mali.gorpad"
data = requests.get("https://scan.seo.com")
soup = bs4.BeautifulSoup(data.text, 'html.parser')
print(soup.prettify())

# # for para in soup.find_all('div'):
# #     print(para)
#
# for para in soup.find_all('div'):
#     print(para.text)
#
# for para in soup.find_all('a'):
#     link = para.get("href")
#     #print(link)
#     if link.startswith("/") and link!="#":
#         print("https://www.facebook.com"+link)
#     elif link=="#":
#         print('https://www.facebook.com/')
#     else:
#         print(link)

# url2 = "https://www.youtube.com/channel/UCi7DM6_Y0EXPdKN_YJIrzKg/videos?disable_polymer=1"
# data = requests.get(url2)
# soup = bs4.BeautifulSoup(data.text, 'html.parser')
# for para in soup.find_all('a'):
#     link = para.get("href")
#     if link.startswith("//www") and link != "#":
#       print("https:" + link)
#     elif link.startswith("http"):
#       print(link)
#     else:
#       print("https://www.youtube.com"+link)