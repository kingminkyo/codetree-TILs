#include <iostream>
#include <unordered_map>

#define MAX_N 100000

using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.

    unordered_map<string, int> map1;
    unordered_map<int, string> map2;

    int n, m; 
    string s; 

    cin >> n >> m; 

    for (int i = 1; i <= n; i++){
        cin >> s;

        map1[s] = i;
        map2[i] = s;
    }

    for (int i = 1; i <= m; i++){
        cin >> s;

        if (s[0] >= '0' && s[0] <= '9'){
            cout << map2[stoi(s)] << endl;
        }
        else{
            cout << map1[s] << endl;
        }
    }

    return 0;
}