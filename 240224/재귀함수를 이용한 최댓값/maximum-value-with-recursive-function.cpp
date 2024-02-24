#include <iostream>
#include <algorithm>

#define MAX 100

using namespace std;

int arr[MAX];

int MaxValue(int a){
    if (a==0)
        return arr[0];

    return max(MaxValue(a-1), arr[a])
}


int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;

    for (int i = 0; i<n; i++){
        cin >> arr[i];
    }

    cout << MaxValue(n-1);
    return 0;
}