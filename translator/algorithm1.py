"""
1. 받침 신공('한국인엗겓받칩닏닫')
"""

def alg1(input):
    #input="훈민 정음"
    n=len(input)
    result=""
    for i in range(n):
        x=input[i]  #문자열 순서대로 추출
        if ord(x)>=44032 and ord(x)<=55203: #한글 음절 범위 내에 있으면 변환, 아니면 그대로 반환 (cf. 가=44032, 힣=55203)
            y=ord(x)+2  #난이도에 따라 +1~3 조절?
            z=chr(y)
        else:
            z=x
        result=result+z
    return result

#a=alg1("훈민정음")
#print(a)
