# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def over_24(people):
    over_24_count = 0 #24세가 넘는 지원자를 카운트 하기 위한 변수 선언
    for old in people: #리스트내 원소(?)를 각각 불러오기
        if old['age'] > 24: #리스트내 딕셔너리에 'age'에 해당하는 값 중 24살이 넘으면
            over_24_count +=1 #1명을 카운드해서 더하는 방식
    return over_24_count


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    people = [
        {'name': '김싸피', 'age': 25},
        {'name': '이싸피', 'age': 28},
        {'name': '조싸피', 'age': 29},
        {'name': '아싸피', 'age': 23},
        {'name': '최싸피', 'age': 22},
        {'name': '고싸피', 'age': 21},
        {'name': '유싸피', 'age': 26},
        {'name': '후싸피', 'age': 20},
    ]

    print(over_24(people))  # 4