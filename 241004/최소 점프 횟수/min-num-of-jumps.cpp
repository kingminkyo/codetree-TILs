#include <iostream>
#include <vector> 
using namespace std;


int n;
vector<int> arr; 

int result = n+1; 

void find_path(int idx, int cnt){


    if (idx >= n-1){
        result = min(result, cnt);
        return;
    }

    // if (arr[idx] == 0) {
    // return;  // 더 이상 전진 불가, 이 경로는 실패.
    // }
    for(int i = 1; i < arr[idx]+1; i++){
        find_path(idx+i, cnt+1);
    }
}

int main() {
    // 여기에 코드를 작성해주세요.
    cin >> n; 
    result = n+1;

    for(int i = 0; i < n; i++){
        int a; 
        cin >> a; 
        arr.push_back(a);
    }

    find_path(0, 0);
    // for (auto a:arr)
    //     cout << a << " ";
    
    if (result == n+1){
        result = -1; 
    }
    cout << result;


    return 0;
}