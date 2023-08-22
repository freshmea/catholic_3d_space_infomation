# a = 'a : {0:.2f} {1:.2f}'
# for i in range(10):
#     print(a.format(i/3, 10))

a = 100
b = 200
# 3.7 이전
print('a: {}\t b: {}'.format(a, b))
# 3.7 이후
print(f'a: {a:.2f}\t b: {b}')


