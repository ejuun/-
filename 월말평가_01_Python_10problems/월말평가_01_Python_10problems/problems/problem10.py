# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def is_position_safe(N, M, position):
    game_list = [[0 for i in range(N)] for i in range(N)] # N x N 행렬 생성
    #(0,0)을 기준으로 오른쪽으로 방향으로 +, 아래방향으로 -로 계산
    if M == 0 or M == 1: #만약 이동 방향이 북 or 남일경우
        if M == 0 : #북이면
            new_lo = position[0] + 1 #윗 방향으로 이동(위로 1더하기)
            if (-N +1) <= new_lo <= 0: #N x N 행렬을 세로선범위 안에 있을경우
                return True
            else:
                return False
        elif M == 1: #남일때
            new_lo = position[0] - 1 #아랫방향으로 이동(아래로 1빼기)
            if (-N +1) <= new_lo <= 0: #범위 안에 있을 때
                return True
            else:
                return False
    elif M == 2 or M == 3: #동서 방향 으로 이동시
        if M == 2: #서로 갔을 때
            new_lo = position[1] - 1 #현위치에서 1만큼빼기
            if 0 <= new_lo <= (N-1): #가로 범위안에 있을 경우
                return True
            else:
                return False
        elif M == 3: #동으로 갔을 때
            new_lo = position[1] + 1 #오른쪽방향이니 1더하기)
            if 0 <= new_lo <= (N-1):
                return True
            else:
                return False


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(is_position_safe(3, 1, (0, 0)))  # True
    print(is_position_safe(3, 0, (0, 0)))  # False