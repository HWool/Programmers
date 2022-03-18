def solution(left, right):
    answer = 0
    for x in range(left,right+1):
        num1 = 0
        for y in range(1,x+1,1):
            if x % y == 0:
                num1 += 1
        if num1 % 2 ==0:
            answer += x
        else:
            answer -= x
    return answer


