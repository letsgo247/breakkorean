"""
2. 된소리 되기('쒸프트키까안빠쪄요')
"""

def alg2(input):
    n=len(input)
    result=""
    for i in range(n):
        x=input[i]  #문자열 순서대로 추출
        if ord(x)>=44032 and ord(x)<=55201: #한글 음절 범위 내에 있으면 변환, 아니면 그대로 반환 (cf. 가=44032, 힐=55201, 힣=55203)
            a=ord(x)    #문자 번호
            b=int((a-44032)/(21*28))    #초성 인덱스
            if b in [0,3,7,9,12]:   #초성이 ㄱ,ㄷ,ㅂ,ㅅ,ㅈ면 (=된소리 가능)
                z=chr(a+21*28)
            else:
                z=x
        else:
            z=x
        result=result+z
    return result
