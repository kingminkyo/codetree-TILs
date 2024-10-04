#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

class Number {
public:
    int number;
    int index;
    Number(int num, int idx) {
        this->number = num;
        this->index = idx;
    }
    Number() {}
};

vector<Number> numbers;
int n;
int num;

bool comp(Number a, Number b) {
    return a.number < b.number;
}

int main() {
    // 입력 받기
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> num;
        numbers.push_back(Number(num, i));  // 숫자와 그에 해당하는 인덱스를 저장
    }

    // 숫자를 정렬 (원래 인덱스를 기억한 채로)
    sort(numbers.begin(), numbers.end(), comp);

    // 결과를 저장할 벡터
    vector<int> result(n);

    // 각 숫자의 원래 인덱스 위치에 정렬 후의 순위를 저장
    for (int i = 0; i < n; i++) {
        result[numbers[i].index] = i + 1;  // 순위는 1부터 시작
    }

    // 결과 출력
    for (int i = 0; i < n; i++) {
        cout << result[i] << " ";
    }

    return 0;
}