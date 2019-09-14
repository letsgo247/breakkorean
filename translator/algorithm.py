"""
1. 받침 신공('한국인엗겓받칩닏닫')
"""

def alg1(input):
    n=len(input)
    result=""
    for i in range(n):
        x=input[i]  #문자열 순서대로 추출
        if ord(x)>=44032 and ord(x)<=55201: #한글 음절 범위 내에 있으면 변환, 아니면 그대로 반환 (cf. 가=44032, 힣=55203)
            y=ord(x)+2  #난이도에 따라 +1~3 조절?
            z=chr(y)
        else:
            z=x
        result=result+z
    return result






"""
2. 된소리 되기('쒸프트키까안빠쪄요')
"""

def alg2(input):
    n=len(input)
    result=""
    for i in range(n):
        x=input[i]  #문자열 순서대로 추출
        if ord(x)>=44032 and ord(x)<=55203: #한글 음절 범위 내에 있으면 변환, 아니면 그대로 반환 (cf. 가=44032, 힐=55201, 힣=55203)
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






"""
3. 자모분리('ㅎㅏㄴㄱㅡㄹㅇㅡㅣㅇㅜㅣㄷㅐㅎㅏㅁ')
"""

def alg3(input):
    n=len(input)
    result=""
    for i in range(n):
        x=input[i]  #문자열 순서대로 추출
        if ord(x)>=44032 and ord(x)<=55203: #한글 음절 범위 내에 있으면 변환, 아니면 그대로 반환 (cf. 가=44032, 힐=55201, 힣=55203)
            a=ord(x)    #문자 번호


            """초성 가즈아"""
            Cho_list=['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']

            b=int((a-44032)/(21*28))    #초성 인덱스
            c=Cho_list[b]   #표준->호환
            #c=b+0x1100  #초성 코드
            #d=chr(c)    #초성 추출
            result=result+c


            """중성 ㅇㅋ"""
            e=int((a-44032)/28%21)  #중성 인덱스
            f=e+0x1161  #중성 코드
            g=chr(f)    #중성 추출
            result=result+g


            """종성 가즈아"""
            Jong_list=['','ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅁ','ㅂ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']

            h=int((a-44032)%28) #종성 인덱스
            k=Jong_list[h]  #표준->호환
            #j=h+0x11A8-1    #종성 코드
            #k=chr(j)    #종성 추출
            result=result+k
        else:
            z=x
            result=result+z
    return result
