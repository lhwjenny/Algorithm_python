n, x = map(int, input().split())
a = list(map(int, input().split()))

for i in range (n) :
    if a[i] < x :
        print(a[i], end=" ") #개행안되게 하는 것.
    