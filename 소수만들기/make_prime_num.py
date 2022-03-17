from itertools import combinations 

def solution(nums):
    my_set = set(nums)
    cmb = list(combinations(my_set,3))
    sum = 0
    li = []
    answer = 0
    for x in range(len(cmb)):
        li.append(list(cmb[x])) 
        for y in range(0,3,1):
            sum += li[x][y]
        print(sum)
        if sum % 2 != 0 and sum % 3 != 0 and sum % 5 != 0:
            answer += 1
        sum = 0
    return answer
nums = [1,2,3,4,10]
print(solution(nums))

#from itertools import combinations          # 중복허용(X), 순서의미(O) 인 조합을 import
#
#"""소수 판별 함수"""
#def is_prime_number(num):
#    if num==0 or num==1:
#        return False
#    else:
#        for n in range(2, (num//2)+1):      # math를 사용하지 않고 (num//2)+1 까지로 설정
#            if num%n == 0:
#                return False
#        
#        return True
#
#def solution(nums):
#    answer = 0
#    cmb = list(combinations(nums,3))        # nums배열을 3개씩 조합 후 list로 변경
#    for arr in cmb:
#        if is_prime_number(sum(arr)):       # cmb를 하나씩 가져와 sum한 값을 소수 판별 함수로 넘겨줌
#            answer += 1                     # return 값이 True이면 count(=answer) +1
#    
#    return answer
#
#
#print(solution([1,2,7,6,4]))



