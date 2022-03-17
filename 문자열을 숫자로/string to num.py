def solution(a):
    answer = ""
    num = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    li = ""
    for x in a:
        li += x
        if li in num.keys():
            answer += str(num[li])
            li = ""
    return answer

a = "onesevenfiveone"
solution(a)
