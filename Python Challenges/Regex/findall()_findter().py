import re

s = '[qwrtypsdfghjklzxcvbnm]'

item = re.findall('(?<=' + s +')([aeiou]{2,})' + s, input(), re.I)

print('\n'.join(item or ['-1']))
