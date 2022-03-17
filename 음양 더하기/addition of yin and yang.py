def solution(absolutes, signs):
    answer = 123456789
    sum = 0
    for x in range(len(absolutes)):
        if signs[x] == False:
            absolutes[x] = -absolutes[x]
        sum += absolutes[x]
    answer = sum
    return answer

absolutes = [1,2,3]
signs = [False,False,True]
print(solution(absolutes,signs))

#def solution(a,b):
#    answer = 0
#    for x in range(len(a)):
#        if b[x] == False:
#            a[x] = -a[x]
#        answer += a[x]
#    return answer
#a = [1,2,3]
#signs = [False,False,True]
#print(solution(a,signs))