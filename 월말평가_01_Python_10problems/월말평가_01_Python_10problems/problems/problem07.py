# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def calculator(*numbers):
    if len(numbers) == 1: #입력값 1개일 경우
        pi = 3.14
        cercle = pi * numbers[0] * numbers[0] #원 넓이 공식 
        return cercle
    elif len(numbers) == 2: #입력값 2개일 경우
        nums_sum = 0
        for i in numbers:
            nums_sum += i #입력값의 합 계산
        if nums_sum % 2 :#합이 홀수면
            return 0.5 * numbers[0] * numbers[1] #삼각형 공식
        else: #짝수
            return numbers[0] * numbers[1] #사각형 공식
    elif len(numbers) == 0: #값이 없으면 
        return 0 #0 반환
    else: #이 외 값이 3개 이상일 경우
        multi_sum = 0
        for num in numbers:
            multi_sum += num #각각의 합
        avg_multi = multi_sum / len(numbers) #입력받은 값의 평균값
        return (multi_sum,avg_multi)


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(calculator(5))                # 78.5
    print(calculator(10, 20))           # 200
    print(calculator(10, 20, 30, 40))   # (100, 25.0)
    print(calculator())                 # 0