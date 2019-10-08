from math import sqrt

num = int(input("输入一个正整数: "))
end = int(sqrt(num))
is_prime = True
for x in range(2,end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print("%d 是素数"%num)
else:
    print("%d不是素数"%num)

if __name__ == '__main__':
    pass
