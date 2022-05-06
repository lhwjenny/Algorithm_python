N = int(input())

for i in range(N) :
    A, B = map(int, input().split())
    C = A + B
    print("Case #%s: %s + %s = %s"%(i+1, A, B, C))