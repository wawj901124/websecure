import requests
from threading import Thread
import sys
import getopt
from termcolor import colored, cprint


class request_performer(Thread):
    def __init__(self,word,url):
        Thread.__init__(self)
        try:
            self.word = word.split("\n")[0]
            self.urly = url.replace('FUZZ',self.word)
            self.url = self.urly
        except Exception as e:
            print(e)

    def run(self):
        try:
            r = requests.get(self.url)
            # 统计网页行数
            lines = str(r.text.count("\n"))
            # 统计网页字符数
            charts = str(len(r._content))
            # 统计网页词数
            words = str(len(re.findall(r"\S+", r.text)))
            # 哈希值
            hashs = str(hashlib.md5(r.content).hexdigest())
            # 状态码
            scode = r.status_code
            if '200' <= scode < '300':
                print(colored(scode,'green') + "\t" + charts + "  \t" + lines + "   \t" + words+" \t"+hashs+"\t"+self.url)
            elif '400' <= scode < '500':
                print(colored(scode,'red') + "\t" + charts + "  \t" + lines + "   \t" + words+" \t"+hashs+"\t"+self.url)
            elif '300' <= scode < '400':
                print(colored(scode,'blue') + "\t" + charts + " \t" + lines + "   \t" + words+" \t"+hashs+"\t"+self.url)
            else:
                print(colored(scode,'yellow') + "\t" + charts + "   \t" + lines + "   \t" + words+" \t"+hashs+"\t"+self.url)
            i[0] = i[0] -1
        except Exception as e:
            print(e)

# 除了添加颜色的显示外，在结果中仅仅显示URL的状态码似乎有点单调，我们再添加几个结果显示：
#
# 网页文本的行数；
# 网页文本的字符数；
# 网页中的词数；
# 网页内容的哈希值；

rr = request_performer()
rr.run()