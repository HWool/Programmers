#def solution(numbers):
#    answer = -1
#    li=[]
#    max = [0,1,2,3,4,5,6,7,8,9]
#    result = []
#    for x in range(0,10,1):
#        for y in range(len(numbers)):
#            if numbers[y] == x:
#                li.append(x)
#    
#    for x in max:
#        if x not in li:
#            result.append(x)
#    for x in range(len(result)):
#        answer += result[x]
#    answer += 1
#
#    return answer

def solution(a):
    answer = 0
    num = [0,1,2,3,4,5,6,7,8,9]
    for x in num:
        if x not in a:
            answer += x
    return answer
a = [1,2,3,4,6,7,8,0]
print(solution(a))