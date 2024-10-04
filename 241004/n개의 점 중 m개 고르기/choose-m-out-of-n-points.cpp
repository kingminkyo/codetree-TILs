#include <iostream>
#include <vector>
#include <tuple>
#include <cmath>

using namespace std;

int n, m;
vector<pair<int, int>> lines; 
vector<pair<int, int>> selected; 


int ucl_dist(pair<int, int> p1, pair<int, int> p2){
    int x1, y1;
    tie(x1, y1) = p1;

    int x2, y2;
    tie(x2, y2) = p2;

    return pow((x1-x2), 2) + pow((y1-y2), 2); 
}





int calc(){
    int result = 0; 
    for(int i = 0; i < m; i++){
        for(int j = i+1; j < m ; j++){
            result = max(result, ucl_dist(selected[i], selected[j]));
        }
    }
    return result; 
}

void selected_print(){
    for(auto a : selected){
        cout << a.first << "/" << a.second << " ";
    cout << endl;
    
    }
}

int result = 10000; 

void choose(int idx, int cnt){
    if (cnt == m){
        // selected_print();
        // cout << "--" << endl; 
        result = min(calc(), result);
        return; 
    }

    if(idx == n)
        return;

    selected.push_back(lines[idx]);
    choose(idx+1, cnt+1);
    selected.pop_back();

    choose(idx+1, cnt); 




}



int main() {
    // 여기에 코드를 작성해주세요.
    cin >> n >> m; 

    for(int i = 0; i < n; i++){
        int a, b;
        cin >> a >> b;

        lines.push_back(make_pair(a, b));
    }


    choose(0, 0);

    cout << result; 
    return 0;
}