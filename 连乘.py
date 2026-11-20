lst = list(map(int, input("请输入若干整数，空格分隔：").split()))
res = 1
for num in lst:
    res *= num
print("连乘的结果：", res)