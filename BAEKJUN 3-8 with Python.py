t = int(input("몇 번 하시겠습니까?"))

i = 0

for i in range(0, t):
    a, b = map(int, input("정수를 입력해주세요").split())
    s = a + b
    i += 1
    print("Case #{0}: {1} + {2} = {3}".format(i, a, b, s))
