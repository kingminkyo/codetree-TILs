#include <iostream>
#include <unordered_map>
using namespace std;

int n, k;

int main() {
    // 여기에 코드를 작성해주세요.

    cin >> n >> k; 

    unordered_map<int, int> m;

    for (int i = 0; i < n; i++){
        int num;
        cin >> num;

        if (m[num])
            m[num] += 1;
        else
            m[num] = 1;
    }

    for (int i = 0; i < k; i++){
        int num;
        cin >> num;

        cout << m[num] <<" ";
    }


    return 0;
}