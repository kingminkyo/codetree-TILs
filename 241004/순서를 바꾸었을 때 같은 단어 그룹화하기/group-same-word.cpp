#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    unordered_map<string, int> words; 

    for(int i = 0; i < n; i++){
        string word;
        cin >> word; 

        sort(word.begin(), word.end());
        words[word]++; 
    }
        int ans = 0;

        for(unordered_map<string, int>::iterator it = words.begin(); it != words.end(); it++){
            ans = max(ans, it->second);
        }

        cout << ans;


    


    return 0;
}