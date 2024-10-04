#include <iostream>
#include <string>
#include <unordered_map> 

using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    string word;
    cin >> word;

    unordered_map<char, int> freq;

    for(char s : word)
        freq[s]++;
    
    bool key = false;
    for(char s : word){
        if (freq[s] == 1){
            cout << s;
            key = true;
            break;
        }
    }
    if (!key)
        cout << "None"; 

    
    

    return 0;
}