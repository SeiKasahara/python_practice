# 插入排序.py2
num = input("请输入数字: ")
num_lst = list(num)

print('排序前：')
print(num_lst)
i = 1
for i in range(len(num_lst)):
    key = num_lst[i]
    j = i - 1
    while j > -1 and num_lst[j] > key:
        num_lst[j+1] = num_lst[j]
        j = j - 1
    num_lst[j+1] = key
print('排序后：')
print(num_lst)

