def keyBoardCheck(res):
    p1 = 0
    p2 = 1
    lst = []
    if len(res) ==0:
        return ""
    if len(res) < 2:
        return res[0]
    while p1 < len(res):
        if res[p1] != res[p2]:
            if res[p1] not in lst:
                lst.append(res[p1])
                p1 += 1
                p2 += 1
            else:
                p1 += 1
                p2 += 1
        else:
            if (len(res) - (p2 + 1)) == 1:
                lst.append(res[p2+1])
                break
            else:
                p1 += 2
                p2 += 2
    lst.sort()
    return "".join(lst)
user_input = input("Enter string: ")
print(keyBoardCheck(user_input))