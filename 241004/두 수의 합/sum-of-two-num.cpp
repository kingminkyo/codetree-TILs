#include <iostream>
#include <unordered_map>
using namespace std;

#define MAX_N 100000

int n, k;
int arr[MAX_N];
unordered_map<int, int> count;


int main() {
    // 여기에 코드를 작성해주세요.

    cin >> n >> k;

    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }

    int ans = 0;

    for(int i = 0; i < n; i++){
        int diff = k - arr[i];

        ans += count[diff];

        count[arr[i]]++;
    }
    cout << ans;
}