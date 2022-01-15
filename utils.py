# 去除字符串首尾空格
def trim(s):
    flag = 0
    if s[:1] == ' ':
        s = s[1:]
        flag = 1
    if s[-1:] == ' ':
        s = s[:-1]
        flag = 1
    if flag == 1:
        return trim(s)
    else:
        return s
# print(trim('  Hello world!  '))

def removeN(s):
    return s.replace("\n", "")