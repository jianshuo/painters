import requests
from bs4 import BeautifulSoup

url = 'https://mp.weixin.qq.com/s/41fG4qjPTbIPXGDs5IGdug'
url = 'https://github.com/jianshuo/painters'
url = 'https://www.zhihu.com/question/20706333'
url = 'https://mp.weixin.qq.com/s/8fbmZz6uPTHFukgwtt2_xA'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
content = soup.find('div', {'class': 'rich_media_content'})

import jieba
from collections import Counter

stopwords = '，,。,的,我,了,是,、,在,“,”,一个,飞镖,有,也,卖,元,这个,就,盘, ,说,？,和'.split(',')

words = jieba.cut(content.text)
words = [w for w in words if w not in stopwords]

cnter = Counter(words)
for word, occur in cnter.most_common(50):
    print(word, occur)

import wordcloud
wc = wordcloud.WordCloud(font_path='YangRenDongZhengBangTi.ttf', width=600, height=400).generate_from_frequencies(cnter)
wc.to_file('wc.jpg')
