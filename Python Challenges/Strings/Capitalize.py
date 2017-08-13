def capitalize(string):
    # l = list(string.split())
    # print(string.title())
    # print(string.split(' '))
    print(' '.join([i.capitalize() for i in string.split(' ')]))

capitalize("hello world  lol")
