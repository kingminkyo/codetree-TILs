#include <iostream>
#include <unordered_map>

using namespace std;

int main() {
    int n;
    cin >> n;

    unordered_map<int, int> point; 

    for (int i = 0; i < n; i++) {
        int x, y;
        cin >> x >> y;

        // find를 사용하여 값이 존재하는지 확인
        if (point.find(x) == point.end()) {
            point[x] = y;  // 값이 없으면 추가
        } else if (point[x] > y) {
            point[x] = y;  // 기존 값보다 작은 경우 갱신
        }
    }

    int ans = 0; 
    for (unordered_map<int, int>::iterator it = point.begin(); it != point.end(); it++) {
        ans += it->second;
    }

    cout << ans;
    return 0;
}