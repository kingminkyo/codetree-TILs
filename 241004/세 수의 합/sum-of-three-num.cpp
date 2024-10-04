#include <iostream>
#include <unordered_map>

using namespace std;

#define MAX_N 1000

int n, k;
int arr[MAX_N];
unordered_map<int, int> freq; 

int main() {
    // 여기에 코드를 작성해주세요.
    cin >> n >> k ;

    for(int i = 0; i < n; i++){
        cin >> arr[i];
        freq[arr[i]]++; 
    }

    int ans = 0; 

    for(int i = 0; i < n; i++){
        
        freq[arr[i]]--;

        for(int j = 0; j < i; j++){
            if(freq[k - arr[i] - arr[j]] > 0){
                ans += freq[k - arr[i] - arr[j]];
            }
        }

    }

    cout << ans; 

    return 0;
}