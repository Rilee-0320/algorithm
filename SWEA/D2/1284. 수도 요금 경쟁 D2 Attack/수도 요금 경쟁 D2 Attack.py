# SWEA 1284 수도 요금 경쟁

T = int(input())

for t in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    # A사의 1L당 요금, B사의 기본요금, 추가 요금이 붙는 기준, 1L당 추가 요금, 종민이의 수도 한 달 사용량을 입력받는다.

    if W > R:
        # B사의 추가 요금이 붙는 기준보다 종민이 사용량이 많을 때
        if P * W > Q + (W - R) * S:
            print(f'#{t} {Q + (W - R) * S}')
        # B사의 요금(기본요금 + 추가 요금((사용량-기본요금 기준 사용량) * 1L당 요금))이 더 저렴하면 해당 가격을 출력한다.
        else:
            print(f'#{t} {P * W}')
        # A사의 요금(사용량 * 1L당 요금)이 더 저렴하면 해당 가격을 출력한다.

    else:
        # B사의 추가 요금이 붙는 기준보다 종민이 사용량이 적을 때
        if P * W > Q:
            print(f'#{t} {Q}')
        # A사의 요금(사용량 * 1L당 요금)이 더 저렴하면 해당 가격을 출력한다.
        else:
            print(f'#{t} {P * W}')
        # B사의 기본요금이 더 저렴하면 해당 가격을 출력한다.
