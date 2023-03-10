# 백준 1063 킹
delta = {'R': (1, 0), 'L': (-1, 0), 'B': (0, -1), 'T': (0, 1), 'RT': (1, 1), 'LT': (-1, 1), 'RB': (1, -1), 'LB': (-1, -1)}
# 8방향 좌표를 키와 함께 딕셔너리에 저장한다.
# x축 방향과 y축 방향 증감을 값으로 한다.

king, stone, N = input().split()
k = [ord(king[0]) - 64, int(king[1])]
s = [ord(stone[0]) - 64, int(stone[1])]
# 킹의 위치, 돌의 위치, 움직이는 횟수 N을 입력받는다.
# 입력받은 킹의 위치, 돌의 위치는 좌표로 변환한다.
# 단, 제일 처음 좌표는 (0,0)이 아니라 (1,1)이다.

for _ in range(int(N)):
    dx, dy = delta[input()]
    nx = k[0] + dx
    ny = k[1] + dy
    # 입력받은 명령에 따라 변경한 좌표를 nx, ny 변수에 저장한다.

    if 0 < nx <= 8 and 0 < ny <= 8:
    # 단, 체스판의 범위를 벗어나지 않아야 한다.

        if nx == s[0] and ny == s[1]:
            sx = s[0] + dx
            sy = s[1] + dy
        # 킹을 명령에 따라 이동시킬 좌표에 돌이 있는 경우 돌도 똑같은 방향으로 움직인다.
            if 0 < sx <= 8 and 0 < sy <= 8:
                k = [nx, ny]
                s = [sx, sy]
            # 단, 돌도 체스판의 범위를 벗어나지 않아야 한다.
        else:
            k = [nx, ny]
        # 그 외의 경우 킹만 움직인다.

print(chr(k[0] + 64) + str(k[1]))
print(chr(s[0] + 64) + str(s[1]))
# 킹과 돌의 최종 좌표를 알파벳, 숫자로 이루어진 위치 정보로 바꾸어 출력한다.