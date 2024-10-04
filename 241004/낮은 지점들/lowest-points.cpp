#include <iostream>
#include <unordered_map>

using namespace std;



int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;

    unordered_map<int, int> point; 

    for (int i = 0; i < n; i++){
        int x, y;
        cin >> x >> y;

        if (!point[x])
            point[x] = y;
        else if(point[x] > y)
            point[x] = y;
    }
    
    int ans = 0; 
    for (unordered_map<int, int>::iterator it = point.begin();
         it != point.end(); it++){
            ans += it->second;
         }
    cout << ans; 
    return 0;
}