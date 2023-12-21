def parenthesesAndBracesChecker(s):
    D = { '[':']' , '(':')' }
    l = []
    for x in s :
        if x in D:
            l.append(x)
        elif x in D.values() :
            if len(l)>0 :
                if D[l[-1]] == x: l.pop()
                else : return False
            else : return False
    return False if l else True


# trues = ["a(aa)aa", "aa(b(cd))e[ab]","([aa(b)c[[aaaaa]]r(d)])"]
# for t in trues :
#     print(parenthesesAndBracesChecker(t))

# falses = ["a([b)]", "((aab)d", "((", "ef)]"]
# for f in falses :
#     print(parenthesesAndBracesChecker(f))