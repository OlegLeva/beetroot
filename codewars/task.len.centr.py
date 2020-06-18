def get_middle(s):
    return s[(len(s) - 1) / 2:len(s) / 2 + 1]
    # l = len(s) + 1
    # sym1 = str(s[0:l // 2][-1])
    # sym2 = str(s[l // 2:][0])
    # if len(s) % 2 == 0:
    #     return sym1 + sym2
    # if len(s) % 2:
    #     return sym1

print(get_middle("asdfdsa"))
