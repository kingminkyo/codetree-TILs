#include <iostream>
#include <algorithm> // min, max 함수 사용
using namespace std;

pair<int, int> game_duration(int m, int a, int b) {
    int min_turns = 1e9; // 최소 횟수는 아주 큰 값으로 초기화
    int max_turns = 0;   // 최대 횟수는 0으로 초기화

    // a부터 b까지의 모든 숫자에 대해 이분 탐색을 수행
    for (int num = a; num <= b; ++num) {
        int turns = 0;
        int left = 1, right = m;

        // 이분 탐색을 진행
        while (left <= right) {
            int mid = (left + right) / 2;
            turns += 1;

            if (mid == num) {
                break;  // 숫자를 찾았을 때
            } else if (mid < num) {
                left = mid + 1;  // num이 더 크면 오른쪽 탐색
            } else {
                right = mid - 1; // num이 더 작으면 왼쪽 탐색
            }
        }

        // 최소 횟수와 최대 횟수를 업데이트
        min_turns = min(min_turns, turns);
        max_turns = max(max_turns, turns);
    }

    return {min_turns, max_turns};
}

int main() {
    int m, a, b;
    cin >> m;
    cin >> a >> b;

    pair<int, int> result = game_duration(m, a, b);
    cout << result.first << " " << result.second << endl;

    return 0;
}