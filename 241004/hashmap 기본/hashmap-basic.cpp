#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    unordered_map<int, int> m; 
    int n;

    cin >> n;

    for (int i = 0; i < n; i++){
        string command;
        int k, v;
        cin >> command; 

        if (command == "add"){
            cin >> k >> v;
            m[k] = v;
        }
        else if (command == "find"){
            cin >> k; 
            if (m[k] == false)
                cout << "None" << endl;
        
            else
                cout << m[k] << endl;
        }
        else if (command == "remove"){
            cin >> k;
            m.erase(k);
        }
    }
    
    return 0;
}