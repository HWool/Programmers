from numpy import sort


def solution(array, commands):
    answer = []
    for i in range(0,len(commands),1): 
        x = commands[i][0]
        x1 = commands[i][1]
        x2 = array[x-1:x1]
        x2.sort()
        x3 = commands[i][2]
        x4 = x2[x3-1]
        answer.append(x4)

    return answer

a = [1,5,2,6,3,7,4]
b = [[2,5,3],[4,4,1],[1,7,3],[2,5,3]]
print(solution(a,b))

#def solution(array, commands):
#    answer = []
#    c = []
#    for x in range(len(commands)):
#        i = commands[x][0]
#        j = commands[x][1]
#        k = commands[x][2]
#        
#        
#        c = array[i-1:j]
#        c.sort()
#        answer.append(c[k-1]) 
#
#    print(answer)
#
#
#    return answer