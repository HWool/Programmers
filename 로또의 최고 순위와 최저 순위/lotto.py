def solution(lottos, win_nums):
    answer = []
    result = []
    num=0
    best = 0
    for x in range(len(lottos)):
        if lottos[x] == 0:
            best += 1
        for y in range(len(win_nums)):           
            if lottos[x] == win_nums[y]:
                num += 1
    best += num
    result.extend([best,num])
    print(result)

    for x in range(len(result)):
        if result[x] == 6:
            answer.append(1)
        elif result[x] == 5:
            answer.append(2)
        elif result[x] == 4:
            answer.append(3)
        elif result[x] == 3:
            answer.append(4)
        elif result[x] == 2:
            answer.append(5)
        else : answer.append(6)
 
    print(answer)
    return answer

#lottos = [44,1,0,0,31,25]
#win_num = [31,10,45,1,6,19]
#solution(lottos,win_num)
#
#def solution(lottos,win_nums):
#    answer=[]
#    low = 0
#    top = 0
#    result = {0:6,1:6,2:5,3:4,4:3,5:2,6:1}
#    for x in lottos:
#        if x in win_nums:
#            low += 1
#        if x == 0:
#           top += 1
#    top += low 
#    if top in result.keys():
#        answer.append(result[top])
#    if low in result.keys():
#        answer.append(result[low])
#    print(answer)
#    return answer
#
#lottos = [0,0,0,0,0,0]
#win_nums=[31,10,45,1,6,19]
#solution(lottos,win_nums)
