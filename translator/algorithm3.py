"""
3. 자모분리('ㅎㅏㄴㄱㅡㄹㅇㅡㅣㅇㅜㅣㄷㅐㅎㅏㅁ')
"""

def alg3(input):
    #input="훈민 정음"
    n=len(input)
    result=""
    for i in range(n):
        x=input[i]  #문자열 순서대로 추출
        if ord(x)>=44032 and ord(x)<=55201: #한글 음절 범위 내에 있으면 변환, 아니면 그대로 반환 (cf. 가=44032, 힐=55201, 힣=55203)
            a=ord(x)    #문자 번호
            b=int((a-44032)/(21*28))    #초성 인덱스
            c=b+0x1100  #초성 코드
            d=chr(c)    #초성 추출
            result=result+d

            e=int((a-44032)/28%21)  #중성 인덱스
            f=e+0x1161  #중성 코드
            g=chr(f)    #중성 추출
            result=result+g

            h=int((a-44032)%28) #종성 인덱스
            if h==0:    #종성 없으면 pass
                pass
            else:
                j=h+0x11A8-1    #종성 코드
                k=chr(j)    #종성 추출
                result=result+k

        else:
            z=x
            result=result+z
        return result
