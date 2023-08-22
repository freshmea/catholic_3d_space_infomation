li = []
li.append(1)
li.append(2)
li.append('string')
li.append(3.1415)
li.append([1,2,3])
# print(li)
# del li[3]
# print(li)
# temp = li.pop(2)
# print(li)
# print(temp)

for i, item in enumerate(li):
    print(i, item)
print('end')