def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for x in range(len(citations)):
        if x+1 <= citations[x]:
            answer += 1
    print(answer)
    return answer

a = [3,0,6,1,5,2,4,7,9]
solution(a)