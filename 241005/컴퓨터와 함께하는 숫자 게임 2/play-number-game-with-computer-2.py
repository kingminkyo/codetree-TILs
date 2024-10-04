def game_duration(m, a, b):
    # 최소 횟수와 최대 횟수를 초기화합니다.
    min_turns, max_turns = float('inf'), 0

    # a부터 b까지의 모든 숫자에 대해 이분 탐색을 수행합니다.
    for num in range(a, b + 1):
        turns = 0
        left, right = 1, m

        # 이분 탐색을 시작합니다.
        while left <= right:
            # 중간값을 구합니다.
            mid = (left + right) // 2
            turns += 1
            if mid == num:
                break
            elif mid < num:
                left = mid + 1
            else:
                right = mid - 1

        # 최소 횟수와 최대 횟수를 업데이트합니다.
        min_turns = min(min_turns, turns)
        max_turns = max(max_turns, turns)

    return min_turns, max_turns

m = int(input())
a, b = map(int, input().split())
min_duration, max_duration = game_duration(m, a, b)
print(min_duration, max_duration)