# for i in range(1000,10000):
#     n14 = int(str(i)[0]) * int(str(i)[1])
#     n34 = int(str(i)[2]) * int(str(i)[3])
#     mx = max(n14, n34)
#     mn = min(n14, n34)
#     c = str(mn) + str(mx)
#     if c == '1214':
#         print(c, i)

# for i in range(100, 1000):
#     a = str(i)[0]
#     b = str(i)[1]
#     c = str(i)[2]
#     mn = min(a,b,c)
#     mx = max(a,b,c)
#     s = (int(a)+int(b)+int(c)) - int(mx) - int(mn)
#     if mn == '0' and s == '0':
#         n1 = mx + str(s)
#         n2 = mx + str(s)
#     elif mn == '0' or s == '0':
#         n1 = mx + str(s)
#         n2 = str(s) + mn
#     else:
#         n1 = mx + str(s)
#         n2 = mn + str(s)
#     r = int(n1) - int(n2)
#     if r == 5:
#         print(r, i)

# N = '123'
# s = 0
# for i in N:
#     s += int(i)
#     print(s)


# N = '123456'
# s = 0
# a = N[1: :2]
# for i in a:
#     s += int(i)
#     print(s)


# for i in range(2,100):
#     s = 0
#     c = 0
#     for a in str(i):
#         if int(a) % 2 == 0:
#             s += int(a)
#     for a in str(i)[1: :2]:
#         c += int(a)
#     d = abs(s - c)
#     if d == 9:
#         print(d, i)

# N = 120
# for i in range(100, 500):
#     P1 = 1
#     P2 = 1
#     for a in str(i):
#         if int(a) % 2 == 0 and a != '0':
#             P1 *= int(a)
#     for a in str(i):
#         if int(a) % 2 != 0:
#             P2 *= int(a)
#     P1 = P1 * 2
#     R = abs(P1 - P2)
#     if R == 29:
#         print(R, i)

# a = 56
# b = bin(a)
# c = oct(a)
# d = hex(a)
# print(b, c, d)
# e = int(b, 2)
# print(e)

for i in range(1, 100):
    b = bin(i)[2: ]
    if i % 3 == 0:
        b += b[-3: ]
    else:
        c = bin((i % 3) * 3)[2: ]
        b += str(c)
    R = int(b, 2)
    if R > 151:
        print(R)
#Ответ: 166
