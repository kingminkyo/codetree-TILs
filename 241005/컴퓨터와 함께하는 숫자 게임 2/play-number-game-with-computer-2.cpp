#include <iostream>
using namespace std;

long long m; 

// target을 맞출 때까지의 이진 탐색 횟수를 반환
long long binary_search(long long target){
    long long left = 1; // 1부터 시작
    long long right = m; // m까지
    long long time = 0;

    while(left <= right){
        time += 1;
        long long mid = left + (right - left) / 2;

        if (mid == target) {
            return time;  // 정답을 맞췄을 때 시간을 반환
        }
        if (mid > target)
            right = mid - 1;
        else
            left = mid + 1;
    }
    return time;  // 이론적으로는 여기까지 오지 않음
}

int main() {
    // 입력
    cin >> m; 

    int a, b;
    cin >> a >> b;

    long long max_t = 0;
    long long min_t = 100000000; // log2(m)으로 충분함

    for(long long i = a ; i <= b ; i++){
        long long time = binary_search(i);
        max_t = max(max_t, time);
        min_t = min(min_t, time);
    }

    cout << min_t << " " << max_t << endl;

    return 0;
}