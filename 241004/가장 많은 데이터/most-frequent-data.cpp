#include <iostream>
#include <unordered_map>
using namespace std;


int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;

    unordered_map<string, int> m;

    int ans = 0;

    for (int i = 0; i < n; i++){
        string color;
        cin >> color;

        if (m[color] == 0)
            m[color] += 1;
        else
            m[color] += 1;

        ans = max(ans, m[color]) ;


    }
    cout << ans; 

    
    return 0;
}