# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
# python 내장함수 min, max 사용 금지
def min_max(scores):
    #최저점 구하기
    min_score = 99999 #매우 큰 숫자 설정
    for num in scores:
        if min_score > num: #초기 설정 값 보다 num이 작은 값이면 
            min_score = num #min_score 값에 num 값 할당
    #최고점 구하기
    max_score = -99999 #매우 작은 숫자 설정
    for num in scores:
        if max_score < num: #초기 설정 값 보다 num이 큰 값이면
            max_score = num #max_score 값에 num 할당
    return (min_score, max_score) #튜플형태 반환       


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    scores = [80, 90, 85, 75]
    print(min_max(scores))    # (75, 90)