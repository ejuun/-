# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def caesar(word, n):
    new_word = ''
    for i in word:
        if ord('a') <= ord(i) <= ord('z'): #소문자일경우
            if ord(i) + n > ord('z'): #알파벳 범위를 벗어 났을때
                n_word = ord(i) + n - ord('z') + 96 #a부터 시작하는 범위로 돌아오는 계산
                new_word += chr(n_word) 
            else:
                new_word += chr(ord(i)+n) #범위를 넘지 않는다면 그대로 계산해서 추가
        elif ord('A') <= ord(i) <= ord('Z'):#대문자일 경우
            if  ord(i) + n > ord('Z'): #알파벳 범위를 벗어 났을때
                n_word = ord(i) + n - ord('Z') + 64 # A부터 시작하는 범위로 돌아오는 계산
                new_word += chr(n_word)
            else:
                new_word += chr(ord(i)+n)#범위를 넘지 않는다면 그대로 계산해서 추가
    return new_word


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(caesar('apple', 5))      # fuuqj
    print(caesar('ssafy', 1))      # ttbgz
    print(caesar('Python', 10))    # Zidryx
