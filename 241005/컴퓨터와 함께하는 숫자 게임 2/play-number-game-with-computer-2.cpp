#include <iostream>
using namespace std;

// 이진 탐색을 통해 target까지 도달할 때의 횟수를 반환
long long binary_search(long long L, long long R, long long target) {
    long long time = 0;
    
    while (L <= R) {
        time += 1;
        long long mid = (L + R) / 2;  // 중간 값 계산
        if (mid == target) {
            return time;  // 타겟을 찾으면 해당 시간을 반환
        } else if (mid > target) {
            R = mid - 1;
        } else {
            L = mid + 1;
        }
    }
    
    return time;  // 정상적으로는 이곳에 도달하지 않음
}

int main() {
    long long m;
    cin >> m;

    long long a, b;
    cin >> a >> b;

    // 최소 탐색 시간: 중앙값에 가까운 값을 선택할 때
    long long min_time = binary_search(1, m, (a + b) / 2);

    // 최대 탐색 시간: 범위의 양 끝을 선택할 때
    long long max_time = max(binary_search(1, m, a), binary_search(1, m, b));

    // 결과 출력
    cout << min_time << " " << max_time << endl;

    return 0;
}