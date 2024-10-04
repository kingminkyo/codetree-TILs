#include <iostream>
#include <unordered_map> 

using namespace std;

#define MAX_N 5000

int A[MAX_N], B[MAX_N], C[MAX_N], D[MAX_N];
unordered_map<int, int> freq;


int n; 

int main() {
    // 여기에 코드를 작성해주세요.
    cin >> n;

    for (int i = 0; i < n; i++) cin >> A[i];
    for (int i = 0; i < n; i++) cin >> B[i];
    for (int i = 0; i < n; i++) cin >> C[i];
    for (int i = 0; i < n; i++) cin >> D[i];

    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            freq[A[i]+B[j]]++;
        }
    }

    int ans = 0; 

    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            if (freq[-C[i]-D[j]] > 0){
                ans += freq[-C[i]-D[j]];

            }
        }
    }
    cout << ans;
    
    return 0;
}