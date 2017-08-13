from collections import OrderedDict

n = int(input())
D = OrderedDict()

for _ in range(n):
    entry = input().split()
    item_name, price = ' '.join(entry[:-1]), entry[-1]
    D[item_name] = D.get(item_name,0) + int(price)

for item, net_price in D.items():
    print(item, net_price)
