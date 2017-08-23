import email.utils, re

for _ in range(int(input())):
    e = email.utils.parseaddr(input())
    if bool(re.match('[a-zA-Z](\w|-|\.)*@[a-zA-Z]*\.[a-zA-Z]{0,3}$',e[1])) :
        print(email.utils.formataddr(e))
