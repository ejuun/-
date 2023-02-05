# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def is_good_rate(movie):
    if movie.get('user_rating') >= 8: #movie내 'user_rating' 키 값 내 value 값이 8이상이면
        return True     #True값 반환
    else: #아니면 
        return False    #False 반환


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    movie = {
            "id": 1,
            "user_rating": 8.1,
            "title": "그리고 내일",
            "overview": "과거보다 더 성장한 당신은 드디어 꿈을 이루게 된다.",
        }

    print(is_good_rate(movie))  # True