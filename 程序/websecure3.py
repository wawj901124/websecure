import sys
from termcolor import colored, cprint

#termcolor，一个用于将输出进行颜色格式化的工具。

text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
print(text)
cprint('Hello, World!', 'green', 'on_red')

print_red_on_cyan = lambda x: cprint(x, 'red', 'on_cyan')
print_red_on_cyan('Hello, World!')
print_red_on_cyan('Hello, Universe!')

for i in range(10):
    cprint(i, 'magenta', end=' ')

cprint("Attention!", 'red', attrs=['bold'], file=sys.stderr)

# 使用termcolor的colored()方法，可以将普通字符格式化为带有颜色的字符，cprint()方法则可以直接打印出特定颜色的字符。
# termcolor自带了八种颜色供我们使用，分别是：
#
# grey：灰色
# red：红色
# green：绿色
# yellow：黄色
# blue：蓝色
# magenta：品红色
# cyan：青色
# white：白色
# 在探测器中，我们使用colored()方法对状态码进行颜色格式化。