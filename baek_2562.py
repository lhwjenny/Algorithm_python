num = []
for j in range(9) :
    i = int(input())
    num.append(i)

print(max(num))
print(num.index(max(num))+1)