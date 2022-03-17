def solution(answers):
    x = 0
    num = 0
    num1 = 1
    sum = [0,0,0]
    user1 = [1,2,3,4,5]
    user2 = [2,1,2,3,2,4,2,5]
    user3 = [3,3,1,1,2,2,4,4,5,5]
    answer = []
    for i in answers:

        if i == user1[num%len(user1)]:
            sum[0]+=1
        if i == user2[num%len(user2)]:
            sum[1]+=1
        if i == user3[num%len(user3)]:
            sum[2]+=1
        num+=1
    for j in sum:
        if x < j:
            x = j
    for z in sum:
        if z == x:
           answer.append(num1) 
        num1 += 1 
    return answer

a = 2,1,2,3,2,4,2,5
print(solution(a))


#def solution(answers):
#    answer = []
#    sum = [0,0,0]
#    num = 1
#    i = 0
#    user1 = [1,2,3,4,5]
#    user2 = [2,1,2,3,2,4,2,5]
#    user3 = [3,3,1,1,2,2,4,4,5,5]    
#    for x in range(len(answers)):
#        if answers[x] == user1[x%len(user1)]:
#            sum[0] += 1
#        if answers[x] == user2[x%len(user2)]:
#            sum[1] += 1
#        if answers[x] == user3[x%len(user3)]:
#            sum[2] += 1
#
#    for y in sum: 
#        if i < y:
#            i = y
#    for z in sum:
#        if i == z:
#            answer.append(num)
#        num += 1
#    return answer