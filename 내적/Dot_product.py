def solution(a, b):
    answer = 1234567890
    sum = 0
    for x in range(len(a)):
        sum += a[x] * b[x]
    answer = sum
    return answer
a = [1,2,3,4]
b = [-3,-1,0,2]
print(solution(a,b))

#def solution(a,b):
#    answer = 0
#    for x in range(len(a)):
#        answer += a[x] * b[x] 
#    return answer
#a = [1,2,3,4]
#b = [-3,-1,0,2] 
#print(solution(a,b))