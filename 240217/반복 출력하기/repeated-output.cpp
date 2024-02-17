#include <iostream>

using namespace std; 

void print_n_lines(int n){
    for(int i = 0; i<n; i++){
        cout << "12345^&*()_";
    }
}

int main() {
    // 여기에 코드를 작성해주세요.
    int input = 0;

    cin >> input;
    print_n_lines(input);
    
    return 0;
}