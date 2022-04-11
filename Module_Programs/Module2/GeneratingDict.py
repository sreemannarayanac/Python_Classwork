def gendict(n):
    dic = {}
    for i in range(1, n+1):
        dic[i]=i**2
    return dic
dic = gendict(10)
print(dic)