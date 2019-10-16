import requests,re,json
from bs4 import BeautifulSoup


# url = 'https://huaban.com/huaban.com/search/?p="动漫"'
#
# response = requests.get(
#     url=url,
#     headers={
#         'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6799.400 QQBrowser/10.3.2908.400'
#     }
# )
#
#
# soup = BeautifulSoup(response.text,'html.parser')
#
#
# print(soup.contents)
# #
# # img_div =soup.find(name='div',attrs={'id':'baidu_image_holder'})
# #
# #
# # ,attrs={'id':'board_pins_waterfall',}
# # img_list = img_div.find_all(name='img')
# # # print(img_list)
# #
# # for img_tag in img_list:
# #     print(img_tag)

url = 'https://huaban.com/favorite/anime/'

response = requests.get(url=url)


print(response.text)
# list = json.loads(response.text)

# print(list[0])











