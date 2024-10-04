#include <iostream>


using namespace std;

#define MAX_N 100000

int arr[MAX_N]; 
int n, m; 

int find(int target){
    int left = 0, right = n-1; 

    while(left <= right){
        int mid = (left + right) / 2;
        if(arr[mid] == target)
            return mid;
        
        if(arr[mid] > target)
            right = mid - 1;
        else
            left = mid + 1;

    }
    return -1; 

}

int main() {
    // 여기에 코드를 작성해주세요.
    
    cin >> n >> m ;
    for (int i = 0; i < n; i++){
        cin >> arr[i];
    }

    for (int i = 0; i < m; i++){
        int num;
        cin >> num;
        cout << find(num) << endl; 

    }



    return 0;
}