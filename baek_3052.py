arr = []
for i in range(10):
    a = int(input())
    arr.append(a % 42)
arr = set(arr) #set은 집합, 즉 중복되지 않은 원소를 얻고자 할 때 사용할 수 있는 python 내장함수.
print(len(arr))