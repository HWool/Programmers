def solution(nums):
    answer=0
    new = list(set(nums))
    for x in new:
        if answer < len(nums)//2:
            answer += 1    
    return answer