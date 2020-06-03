# 《黑客与画家的Python入门课》

如果问我一个场景，我希望这门课的场景不像大学里面的课堂去学习一门技巧，毕竟两个小时不足放进去太多实际的技巧，而更像是到一个酿酒场参观，通过看到一个技术世界的人是怎么思考这个世界的。

但同时这门课也还是希望尽量有用。技术的世界的一大好处就是每个人都在努力让别人的工作变得简单，电脑的世界像一座大厦一样，每个人都在前人的基础上添砖加瓦。所以这次我会反其道而行之，不是从最简单的，而是从很实用，本来应该是很复杂的部分讲起。

还有一个声明，就是我以天然逻辑为优先，可能不会尊重时间的限制。如果需要更多的时间，我会直接延长或者开系列的课，而不会局限在两个小时以内。

将会涵盖的内容：

## 第一部分，Python基础

1.传说中的“Hello World”。

帮助大家打印出来自己的Hello World。为什么这个词在程序员的世界里面那么
的特殊。这一部分教会大家如何运行一个Python程序。程序和电脑的关系，程序
和程序员的关系，还有程序和这个世界的其他的程序的关系。

1. 起名字。

为什么传说中说“编程问题归根到底是命名问题”。在编程的时候，我们无时无刻
不在给别人起名字。我们这一个部分会讲，在Python里面，如何用名字来装东西
如何把句子装到名字里面。如何把名字装到其他的名字里面。以及名字和名字的
关系。

1. Python里面除了名字以外唯一需要认识的那是十个单词。

只有这几个单词（33个。但实际上常用的10个以内）才是语言的一部分。其他的都
是自己或者别人给起的名字。通过认识这十个单词来认识一门语言。

if, else
for, in
and, or, not
def, import, as

可以说，认识了这十个单词，你就可以说你会Python语言了。之后遇到的所有的
名字，都是别人命名的，可以叫这个，也可以叫其他的名字。

1. 学会用一个布袋子，就是列表[ ]

用一个布袋子可以把很多东西装到一个袋子里面。这样子就可以处理文本了。


1. 装箱。打包再打包。

把自己的程序放在一个箱子里面，让自己用起来方便，让别人用起来方便。这里
介绍用 def 来定义函数，来调用函数。

## 第二部分，不管三七二十一直接冲到深水区

1. 任务一，发邮件

这里会和大家聊一聊编程界的知识领域。HTML是画网页的，Python是做后端的，
互联网协议是专门的领域，比如SMTP等等。Python仅仅是众多的领域中间的一
部分。看这一部分可其他的部分有什么联系。

  > pip install yagmail

这部分我们会讲程序员世界的协作，讲开源运动，讲Python的流行的原因。Python
的世界有自己的App Store。只不过这个App Store是命令行的，是任何一个程序
员可以访问所有其他人的工作，这是世界上最重大的协作之一。

  import yagmail

  username = 'embarazada@qq.com'
  passwod = 'hlnixpqgqwwpbchd'
  server = 'smtp.qq.com'
  mail = yagmail.SMTP(username, password, server)

  to = 'jianshuo@icloud.com'
  subject = 'Hello Jian Shuo'
  body = 'How are you doing? Como estas?'
  mail.send(to, subject, body)

1. 任务二，简单文字处理

Python是文字处理之王。这里简单的展示一下如何用简单的代码来处理文章，
把一个初中的生词表变成一个规整的列表
```
  s = '''内容
  内容
  内容'''
  for s in s.splitlines():
    s = s.strip()
    print(s)
```
3. 任务三，从网页上面拿内容下来
```
  import requests

  url = 'https://zhuanlan.zhihu.com/smetalk'
  response = requests.get(url)
  print(response.text)
```
  手工的任务是如何自动化的

1. 任务三：从网页上获取信息并且找到自己要的部分，然后发邮件
```
  from bs4 as BeautifulSoup

  soup = BeatifulSoup(response.text, 'html.parser')
  for title in soup.findall('h3'):
    print(title)

  mail.send()
```
1. 任务四，分析热词，给自己发邮件。

  这个是最后一个任务了。我们会从微博的一个评论里面来分析词的频率，
  这个其实是对于提供者科技含量很高，对于使用者
  科技含量很低的任务，当然大多数的库都是这样的。
```
  import jieba

  words = jieba.cut(content)
  c = Counter(words)
```
## 第三部分：程序员的世界很好懂。

这部分用来回答大家的问题，还有接受更多的问题。已经准备好的问题包括：
1. 如何客服学习一门语言从入门到放弃？
1. 如何根据自己的情况选择学习哪种语言？
1. 如何分辨和结识大牛？
