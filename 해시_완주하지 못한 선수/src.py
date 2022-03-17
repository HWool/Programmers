def solution(a,b):
    a.sort()
    b.sort()
    answer = a[-1]

    for x in range(len(b)):
        if a[x] != b[x]:
            answer = a[x]
            break
    return answer