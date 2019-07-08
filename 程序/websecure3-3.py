import requests
from threading import Thread
import sys
import getopt
from termcolor import colored, cprint

# 程序标识
def banner():
    print("\n********************")
    name = '''
  ______          _     _
 |___  /         (_)   | |
    / / _ __ ___  _ ___| |_ ___ _ __
   / / | '_ ` _ \| / __| __/ _ \ '__|
  / /__| | | | | | \__ \ ||  __/ |
 /_____|_| |_| |_|_|___/\__\___|_|
    '''
    print(name)
    print("州的先生-暴力发掘器 v0.1")
    print("***********************")


# 程序用法
def usage():
    print("用法：")
    print("     -w:网址 (http://wensite.com/FUZZ)")
    print("     -t:线程数")
    print("     -f:字典文件")
    print("例子：bruteforcer.py -w http://bxu2713810459.my3w.com/FUZZ -t 5 -f commom.txt")
    # -w来指定网址
    # -t来指定线程数
    # -f来指定字典文件


class request_performer(Thread):
    def __init__(self,word,url,hidecode):
        Thread.__init__(self)
        try:
            self.word = word.split("\n")[0]
            self.urly = url.replace('FUZZ',self.word)
            self.url = self.urly
            self.hidecode = hidecode
        except Exception as e:
            print(e)

    def run(self):
        try:
            r = requests.get(self.url)
            # 统计网页行数
            lines = str(r.text.count("\n"))
            # 统计网页字符数
            charts = str(len(r.text))
            # 统计网页词数
            words = str(len(re.findall(r"\S+", r.text)))
            # 哈希值
            hashs = str(hashlib.md5(r.content).hexdigest())
            # 状态码
            scode = str(r.status_code)
            if scode != str(self.hidecode):
                if '200' <= scode < '300':
                    print(colored(scode,
                                  'green') + "\t" + charts + "  \t" + lines + "   \t" + words + " \t" + hashs + "\t" + self.url)
                elif '400' <= scode < '500':
                    print(colored(scode,
                                  'red') + "\t" + charts + "  \t" + lines + "   \t" + words + " \t" + hashs + "\t" + self.url)
                elif '300' <= scode < '400':
                    print(colored(scode,
                                  'blue') + "\t" + charts + " \t" + lines + "   \t" + words + " \t" + hashs + "\t" + self.url)
                else:
                    print(colored(scode,
                                  'yellow') + "\t" + charts + "   \t" + lines + "   \t" + words + " \t" + hashs + "\t" + self.url)
            i[0] = i[0] - 1
        except Exception as e:
            print(e)

def start(argv):
    banner()
    if len(sys.argv) < 5:
        usage()
        sys.exit()
    try:
        opts,args = getopt.getopt(argv,"w:t:f:c:")
    except getopt.GetoptError:
        print("错误的参数")
        sys.exit()
    hidecode = 000
    for opt,arg in opts:
        if opt == '-w':
            url = arg
        elif opt == '-f':
            dicts = arg
        elif opt == '-t':
            threads = arg
        elif opt == '-c':
            hidecode = arg

    try:
        f = open(dicts,'r')
        words = f.readlines()
    except:
        print("打开文件错误：",dicts,"\n")
        sys.exit()

    launcher_thread(words,threads,url,hidecode)


def launcher_thread(names,th,url,hidecode):
    global i
    i = []
    resultlist = []
    print("==============================================")
    print("状态码"+"\t"+"字符数"+"\t"+"行数"+"\t"+"词数"+"\t"+"MD5"+"\t"+"网址")
    print("==============================================")
    i.append(0)
    while len(names):
        try:
            if i[0] < int(th):
                n = names.pop(0)
                i[0] = i[0]+1
                thread = request_performer(n,url,hidecode)
                thread.start()
        except KeyboardInterrupt:
            print("用户停止了程序运行。完成探测")
            sys.exit()
    return True

if __name__ == '__main__':
    try:
        start(sys.argv[1:])
    except KeyboardInterrupt:
        print("用户停止了程序运行。完成探测")


