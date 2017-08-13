def minion_game(string):
    clist = 0
    vlist = 0
    for i in range(len(string)):
        if any(string[i] == v for v in ['A','E','O','U','I']):
            # vlist = string[start:end + 1]
            vlist += len(string) - i
            # print(vlist)
        else:
            # vlist = string[start:end + 1]
            clist += len(string) - i
            # print(clist)
            # print("clist: %d, vlist: %d" % (clist, vlist))

    if clist > vlist:
        print("Stuart %d" % clist)
    elif vlist > clist:
        print("Kevin %d" % vlist)
    else:
        print("Draw")

minion_game("BANANA")
