c = int(input())

for i in range(c) :
    num = list(map(int, input().split()))
    avg = sum(num[1:])/num[0]
    cnt = 0
    for score in num[1:]:
        if score > avg:
            cnt += 1
    rate = (cnt / num[0]) * 100
    print('%.3f' %rate + '%')

