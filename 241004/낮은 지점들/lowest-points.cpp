#include <iostream>
#include <unordered_map>

using namespace std;

int main() {
    int n;
    cin >> n;

    unordered_map<int, int> point;  // x좌표를 키로, y값을 저장

    for (int i = 0; i < n; i++) {
        int x, y;
        cin >> x >> y;

        // 해당 x좌표에 y값이 없으면 추가, 있으면 더 작은 값으로 갱신
        if (point.find(x) == point.end() || point[x] > y) {
            point[x] = y;
        }
    }

    int ans = 0;
    // 남아있는 y값의 합을 구함
    for (auto it = point.begin(); it != point.end(); it++) {
        ans += it->second;
    }

    cout << ans << endl;

    return 0;
}