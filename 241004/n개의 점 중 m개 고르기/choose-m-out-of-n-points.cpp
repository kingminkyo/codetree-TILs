#include <iostream>
#include <vector>
#include <tuple>
#include <cmath>

using namespace std;

int n, m;
vector<pair<int, int>> lines; 



int ucl_dist(pair<int, int> p1, pair<int, int> p2){
    int x1, y1;
    tie(x1, y1) = p1;

    int x2, y2;
    tie(x2, y2) = p2;

    return pow((x1-x2), 2) + pow((y1-y2), 2); 
}



int calc(){
    int result; 
    for(int i = 0; i < n; i++){
        for(int j = i+1; j < n ; j++){
            result = max(result, ucl_dist(lines[i], lines[j]));
        }
    }
    return result; 
}






int main() {
    // 여기에 코드를 작성해주세요.
    cin >> n >> m; 

    for(int i = 0; i < n; i++){
        int a, b;
        cin >> a >> b;

        lines.push_back(make_pair(a, b));
    }


    cout << calc(); 


    return 0;
}