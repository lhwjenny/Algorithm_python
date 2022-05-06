n = int(input())
score = list(map(int, input().split()))
max_s = max(score)

for i in score:
    score.append(i/max_s*100)
avg = sum(score)/n
print(avg)
#---------메모리 초과 문제 발생------------------

N = int(input())
M = list(map(int, input().split())) 
max_ = max(M) 

for i in range(N): 
    M[i] = M[i]/max_*100 
print("%.2f" %(sum(M)/ N))

