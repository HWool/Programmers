#def solution(numbers):
#    length = len(numbers) - 1
#    answer = ''
#    sum = ''
#    for x in range(length):
#        for y in range(length-x):
#  
#            if str(numbers[y]) + str(numbers[y+1]) < str(numbers[y+1])+str(numbers[y]):
#                numbers[y], numbers[y+1] = numbers[y+1], numbers[y]
#                
#    for i in range(len(numbers)):
#        sum += str(numbers[i])
#
#    answer = sum
#    return answer
#
#a = [3,30,34,5,9]
#solution(a)
#




#def bubble_sort(li):
#    sum = ''
#    length = len(li) - 1
#    for i in range(length):
#        for j in range(length-i):
#            if str(li[j])+str(li[j+1]) < str(li[j+1])+str(li[j]):
#                li[j], li[j+1] = li[j+1], li[j]
#    
#    for x in range(len(li)):
#        sum += str(li[x])
#    print(sum)
#
#if __name__ == "__main__":
#    li = [10,2,3,4,1,7,0]
#    bubble_sort(li)


import functools


def compare(x,y):
    if x + y < y + x:
        return +1
    else: return -1

def solution(numbers):
    answer = ''
    list = []
    for i in range(len(numbers)):
        list.append(str(numbers[i]))
    c = sorted(list,key=functools.cmp_to_key(compare))
    for j in range(len(c)):
        answer += c[j]
    if answer[0] == "0":
        return "0"
    return answer

a = [0,3,30,34,5,9]
solution(a)