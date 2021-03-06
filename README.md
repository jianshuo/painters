# 《黑客与画家的Python入门课》

如果问我一个场景，我希望这门课的场景不像大学里面的课堂去学习一门技巧，毕竟两个小时不足放进去太多实际的技巧，而更像是到一个酿酒场参观，通过看到一个技术世界的人是怎么思考这个世界的。

但同时这门课也还是希望尽量有用。技术的世界的一大好处就是每个人都在努力让别人的工作变得简单，电脑的世界像一座大厦一样，每个人都在前人的基础上添砖加瓦。所以这次我会反其道而行之，不是从最简单的，而是从很实用，本来应该是很复杂的部分讲起。

还有一个声明，就是我以天然逻辑为优先，可能不会尊重时间的限制。如果需要更多的时间，我会直接延长或者开系列的课，而不会局限在两个小时以内。

将会涵盖的内容：

## 第一部分，Python基础

### 传说中的“Hello World”

帮助大家打印出来自己的Hello World。为什么这个词在程序员的世界里面那么
的特殊。这一部分教会大家如何运行一个Python程序。程序和电脑的关系，程序
和程序员的关系，还有程序和这个世界的其他的程序的关系。

```python
print('****************************************')
print('Hello World')
print('*' * 40)
```

### 起名字

为什么传说中说“编程问题归根到底是命名问题”。在编程的时候，我们无时无刻
不在给别人起名字。我们这一个部分会讲，在Python里面，如何用名字来装东西
如何把句子装到名字里面。如何把名字装到其他的名字里面。以及名字和名字的
关系。
```python
# 计算机科学里面最难的两件事情，一件事缓存过期问题，一件事命名问题

greetings = 'Hello, World!'
name = '小机器人笨笨'
introduction = '我的名字是' + name
age = '3'
occupation = '机器人'
bye = '*' * 20

print(greetings)
print(introduction)
print('我' + age + '岁了')
print('我是做' + occupation + '工作的')
print(bye)
```

### 学会用一个布袋子，就是列表[ ]

用一个布袋子可以把很多东西装到一个袋子里面。这样子就可以处理文本了。

### Python里面除了名字以外唯一需要认识的那是十个单词

只有这几个单词（33个。但实际上常用的10个以内）才是语言的一部分。其他的都
是自己或者别人给起的名字。通过认识这十个单词来认识一门语言。
```python
if
else
for
in
and
or
not
def
import
as
```
可以说，认识了这十个单词，你就可以说你会Python语言了。之后遇到的所有的
名字，都是别人命名的，可以叫这个，也可以叫其他的名字。

### 装箱。打包再打包

把自己的程序放在一个箱子里面，让自己用起来方便，让别人用起来方便。这里
介绍用 def 来定义函数，来调用函数。

```python
# These are the functions

def greetings(name):
    if name == 'Jian Shuo':
        print('Long time no see.', 'How are you ding?', name)
    else:
        print(name, 'How are you doing?')

def greetsMyself():
    greetings('Jian Shuo')

greetings('John')
greetsMyself()
```

## 第二部分，不管三七二十一直接冲到深水区

### 任务一，发邮件

这里会和大家聊一聊编程界的知识领域。HTML是画网页的，Python是做后端的，
互联网协议是专门的领域，比如SMTP等等。Python仅仅是众多的领域中间的一
部分。看这一部分可其他的部分有什么联系。

> pip3 install yagmail

这部分我们会讲程序员世界的协作，讲开源运动，讲Python的流行的原因。Python
的世界有自己的App Store。只不过这个App Store是命令行的，是任何一个程序
员可以访问所有其他人的工作，这是世界上最重大的协作之一。
```python
import yagmail

username = 'embarazada@qq.com'
password = 'hlnixpqgqwwpbchd'
server = 'smtp.qq.com'
mail = yagmail.SMTP(username, password, server)

to = 'jianshuo@icloud.com'
subject = 'How are you doing today?'
mail.send(to, subject, body)
print('Message [' + subject + '] sent to ' + to)

```

### 任务二，从网页上面拿内容下来
```python
  import requests

  url = 'https://zhuanlan.zhihu.com/smetalk'
  response = requests.get(url)
  print(response.text)
```
  手工的任务是如何自动化的

### 任务三：从网页上获取信息并且找到自己要的部分，然后发邮件

```python
 import requests
from bs4 import BeautifulSoup


resp = requests.get('https://s.weibo.com/realtime?q=%23姜潮妈妈婚前给麦迪娜买房%23&rd=realtime&tw=realtime&Refer=weibo_realtime')
soup = BeautifulSoup(resp.text, 'html.parser')
card = soup.find('div', attrs={'class': 'card-wrap'}).find('p', attrs={'class':'txt'})
latest = card.text.replace(' ', '').replace('\n', '')
print(latest)

import yagmail

username = 'embarazada@qq.com'
password = 'hlnixpqgqwwpbchd'
server = 'smtp.qq.com'
mail = yagmail.SMTP(username, password, server)

to = 'jianshuo@icloud.com'
subject = 'How are you doing today?'
mail.send(to, subject, body)
print('Message [' + subject + '] sent to ' + to)
```

### 任务四，分析热词，给自己发邮件。

  这个是最后一个任务了。我们会从微博的一个评论里面来分析词的频率，
  这个其实是对于提供者科技含量很高，对于使用者
  科技含量很低的任务，当然大多数的库都是这样的。
```python
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
import os
os.system('open wc.jpg')

```

## 第三部分：程序员的世界很好懂。

这部分用来回答大家的问题，还有接受更多的问题。已经准备好的问题包括：
1. 如何客服学习一门语言从入门到放弃？
1. 如何根据自己的情况选择学习哪种语言？
1. 如何分辨和结识大牛？

## 第四部分：课前准备

### 上课前，需要大家准备这些内容：

1. 电脑。根据调查，绝大多数同学是Mac电脑。这是最好，因为Python和Mac非常兼容，相处得很好。Windows电脑也没问题。我的目标还是让大家在上课的时候就把程序跑起来，下课了就可以自己完成以上的那些复杂的任务了。
2. 安装Python。到这里 https://www.python.org/downloads/ 下载并安装Python，有Mac版本和Windows版本。最好安装最新版本3.8.3。对于初学者版本差异不那么大。
3. 安装一个好的编辑器。任何可以编辑**纯文本**的编辑器都可以。但是Word不行，任何可以编辑出来不同大小的字体，为字体加一个下划线的编辑器都 不 可 以。我推荐使用Atom，下载地址 https://atom.io 有Mac，Windows等各种版本。这个编辑器和Python没关系，但是是很好用的简单的编辑器

### 上课前需要大家准备这些知识：
大家看一下这个列表，看看有哪些是自己已经知道的，哪些还不知道。不知道的可以提前熟悉起来

1. 你知道怎么打开你的电脑的命令行吗？

在Mac电脑上，在Spotlight里面（就是最右上角的那个小放大镜图标点一下），输入“Terminal”（只要输入Ter就应该自动的出来了。接下来执行都是在Terminal里面的。不知道的赶紧去打开，打开了以后不知道干什么试着打一个`ls`试试

在Windows电脑上，他的名字叫`CMD`，在运行里面输入就好。`CMD`里面你可以输入`DIR`

然后你就进入了黑黑的DOS时代了。如果不会打开命令行，就跟手机不知道屏幕在哪里一样，以后的一切都没法开始了。

2. 你知道如果你编辑了一个文件，怎么可以在命令行找到吗？

在这一步，我们会用文本编辑器编辑一个文件，你需要在命令行进入这个文件所在的文件夹。找到你写好的Python文件是运行一个Python文件的前提。

如果你对这个不熟悉，可以这样做：你用编辑器（推荐Atom）编辑一个文件，然后把它放在你的桌面上。然后进入你的命令行，输入
```
cd Desktop
```
注意：大小写很重要，cd 小写, D 大写，用`ls`列表命令你就看得到刚刚的那个文件了
