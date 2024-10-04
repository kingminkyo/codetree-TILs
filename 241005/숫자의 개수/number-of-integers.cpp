#include <iostream>
using namespace std;

#define MAX_N 100000

int arr[MAX_N];
int n, m;

int lowerbound(int target){
    int left = 0;
    int right = n-1 ;
    int min_idx = n; 

    while(left <= right){
        int mid = (left + right) / 2; 
        if (arr[mid] >= target){
            right = mid - 1;
            min_idx = min(min_idx, mid);
        }
        else
            left = mid + 1;

    }
    return min_idx;   
}


int upperbound(int target){
    int left = 0;
    int right = n-1 ;
    int min_idx = n; 

    while(left <= right){
        int mid = (left + right) / 2; 
        if (arr[mid] > target){
            right = mid - 1;
            min_idx = min(min_idx, mid);
        }
        else
            left = mid + 1;

    }
    return min_idx;   
}
int main() {
    // 여기에 코드를 작성해주세요.
    cin >> n >> m; 
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }

    for(int i = 0; i < m; i++){
        int x;
        cin >> x;
        int count = upperbound(x) - lowerbound(x);
        cout << count << endl; 

    }

    return 0;
}