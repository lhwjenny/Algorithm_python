cnt = int(input())
numbers = list(map(int, input().split()))
max = numbers[0]
min = numbers[0]

#파이썬에서 list for문으로 사용하는 방법
# for 변수 in 리스트:
for i in numbers[1:]:
    if i>max:
        max = i
    elif i<min:
        min = i
print(min, max)
#------------------------------------------
#두번째 방법
N = int(input())
array = list(map(int, input().split()))
print(min(array), max(array)) #내장함수 쓴거임