lstA = list(map(int, input("请输入列表lstA，整数用空格隔开：").split()))
lstB = list(map(int, input("请输入列表lstB，整数用空格隔开：").split()))
n = min(len(lstA), len(lstB))
result = {}
for i in range(n):
    result[lstA[i]] = lstB[i]
print("生成的字典：", result)