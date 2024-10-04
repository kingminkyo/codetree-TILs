#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>


using namespace std;

#define MAX_N 100000


int main() {
    // 여기에 코드를 작성해주세요.
    int n, k;
    cin >> n >> k; 

    unordered_map<int, int> freq;
    vector<pair<int, int>> v;
    int arr[MAX_N];

    for(int i = 0; i < n; i++){
        cin >> arr[i];
        freq[arr[i]]++;
    }

    for(unordered_map<int,int>::iterator it = freq.begin(); it != freq.end(); it++){
        v.push_back(make_pair(it->second, it->first));
    }

    sort(v.begin(), v.end(), greater<pair<int, int>>());

    for(int i = 0; i < k; i++){
        cout << v[i].second << " " ;
    }



    return 0;
}