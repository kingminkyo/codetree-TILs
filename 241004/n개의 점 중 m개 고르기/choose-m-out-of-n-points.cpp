#include <iostream>
#include <vector>
#include <tuple>
#include <cmath>  // sqrt 함수 사용을 위해 포함

using namespace std;

int n;
vector<pair<int, int>> lines; 

// 두 점 사이의 거리 제곱합을 계산하는 함수
int squared_distance(pair<int, int> p1, pair<int, int> p2) {
    int x1, y1;
    tie(x1, y1) = p1;

    int x2, y2;
    tie(x2, y2) = p2;

    return pow((x1 - x2), 2) + pow((y1 - y2), 2); 
}

// 가장 가까운 두 점 사이의 거리 제곱합을 구하는 함수
int calc() {
    int result = INT_MAX;  // 비교를 위한 매우 큰 값
    for(int i = 0; i < n; i++) {
        for(int j = i + 1; j < n; j++) {
            result = min(result, squared_distance(lines[i], lines[j]));
        }
    }
    return result; 
}

int main() {
    // 입력 처리
    cin >> n;  // m은 필요 없으므로 제거

    for(int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b;
        lines.push_back(make_pair(a, b));
    }

    int min_squared_dist = calc();  // 최단 거리 제곱합 계산
    cout << "최단 거리 제곱합: " << min_squared_dist << endl;

    cout << "최단 거리: " << sqrt(min_squared_dist) << endl;  // 제곱근 계산하여 출력

    return 0;
}