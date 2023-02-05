# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
# 반드시 재귀함수로 구현해야 합니다.
def dec_to_bin(number):
    if number //2 == 1: #만약 몫이 1이라면 나누는 것이 마지막이기때문에
        return str(1) +str(number%2) # 몫인 1과 나머지를 반환
    else:
        return dec_to_bin(number//2) +str(number%2) #몫이 1이 될때까지 반복하는 재귀함수와 2진수 반환을 위한 나머지를 더하기
#맨 뒤에서부터 나머지값이 쌓여간다

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(dec_to_bin(10))  # 1010
    print(dec_to_bin(5))   # 101
    print(dec_to_bin(50))  # 110010